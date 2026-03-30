from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

if __package__ in (None, ""):
    project_root = Path(__file__).resolve().parents[2]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    from src.retail_intel.config import BASE_DIR, get_settings
    from src.retail_intel.data_generator import generate_sales_data
    from src.retail_intel.db import append_table, execute_sql_file, get_engine
else:
    from .config import BASE_DIR, get_settings
    from .data_generator import generate_sales_data
    from .db import append_table, execute_sql_file, get_engine


def clean_sales_data(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    cleaned = frame.copy()
    cleaned["date"] = pd.to_datetime(cleaned["date"])
    cleaned["product"] = cleaned["product"].str.strip()
    cleaned["category"] = cleaned["category"].str.title()
    cleaned["supplier"] = cleaned["supplier"].str.strip()
    cleaned["store_location"] = cleaned["store_location"].str.strip()
    cleaned["payment_type"] = cleaned["payment_type"].str.title()
    cleaned["quantity"] = cleaned["quantity"].clip(lower=0).astype(int)
    cleaned["price"] = cleaned["price"].clip(lower=0).astype(float)
    cleaned["stock_on_hand"] = cleaned["stock_on_hand"].clip(lower=0).astype(int)
    cleaned["revenue"] = cleaned["quantity"] * cleaned["price"]
    cleaned = cleaned.drop_duplicates(subset=["date", "product", "store_location", "payment_type"], keep="last")

    dim_product = (
        cleaned[["product", "category", "supplier", "price"]]
        .sort_values(["product", "price"])
        .groupby(["product", "category", "supplier"], as_index=False)["price"]
        .median()
        .rename(columns={"product": "product_name", "price": "default_unit_price"})
        .reset_index(drop=True)
    )
    dim_product.insert(0, "product_id", range(1, len(dim_product) + 1))

    dim_store = (
        cleaned[["store_location", "city", "township"]]
        .drop_duplicates()
        .sort_values("store_location")
        .rename(columns={"store_location": "store_name"})
        .reset_index(drop=True)
    )
    dim_store.insert(0, "store_id", range(1, len(dim_store) + 1))

    fact_sales = (
        cleaned.merge(dim_product[["product_id", "product_name"]], left_on="product", right_on="product_name")
        .merge(dim_store[["store_id", "store_name"]], left_on="store_location", right_on="store_name")
        .loc[
            :,
            [
                "sale_id",
                "date",
                "product_id",
                "store_id",
                "quantity",
                "price",
                "revenue",
                "stock_on_hand",
                "payment_type",
            ],
        ]
        .rename(columns={"date": "sale_date", "price": "unit_price"})
        .sort_values(["sale_date", "sale_id"])
        .reset_index(drop=True)
    )
    fact_sales["sale_date"] = fact_sales["sale_date"].dt.date

    return dim_product, dim_store, fact_sales


def save_outputs(dim_product: pd.DataFrame, dim_store: pd.DataFrame, fact_sales: pd.DataFrame) -> None:
    settings = get_settings()
    dim_product.to_csv(settings.product_dim_path, index=False)
    dim_store.to_csv(settings.store_dim_path, index=False)
    fact_sales.to_csv(settings.processed_data_path, index=False)


def load_to_postgres(dim_product: pd.DataFrame, dim_store: pd.DataFrame, fact_sales: pd.DataFrame) -> bool:
    settings = get_settings()
    engine = get_engine(settings.database_url)
    if engine is None:
        return False

    schema_path = BASE_DIR / "sql" / "schema.sql"

    try:
        with engine.begin() as connection:
            connection.exec_driver_sql("DROP TABLE IF EXISTS fact_sales")
            connection.exec_driver_sql("DROP TABLE IF EXISTS dim_store")
            connection.exec_driver_sql("DROP TABLE IF EXISTS dim_product")

        execute_sql_file(engine, schema_path)
        append_table(engine, "dim_product", dim_product)
        append_table(engine, "dim_store", dim_store)
        append_table(engine, "fact_sales", fact_sales)
        return True
    except Exception:
        return False


def run_pipeline() -> dict[str, object]:
    settings = get_settings()
    raw_frame = generate_sales_data(days=settings.days_of_history, seed=settings.random_seed)
    raw_frame.to_csv(settings.raw_data_path, index=False)

    dim_product, dim_store, fact_sales = clean_sales_data(raw_frame)
    save_outputs(dim_product, dim_store, fact_sales)
    db_loaded = load_to_postgres(dim_product, dim_store, fact_sales)

    return {
        "raw_rows": len(raw_frame),
        "fact_rows": len(fact_sales),
        "products": len(dim_product),
        "stores": len(dim_store),
        "db_loaded": db_loaded,
        "processed_path": str(settings.processed_data_path),
    }


if __name__ == "__main__":
    result = run_pipeline()
    print(result)
