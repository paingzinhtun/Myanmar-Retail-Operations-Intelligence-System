from __future__ import annotations

import sys
from textwrap import dedent
from pathlib import Path

import pandas as pd
import streamlit as st

if __package__ in (None, ""):
    project_root = Path(__file__).resolve().parents[2]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    from src.retail_intel.config import get_settings
    from src.retail_intel.db import get_engine, read_sql
else:
    from .config import get_settings
    from .db import get_engine, read_sql


def fetch_dataframe(query: str) -> pd.DataFrame:
    settings = get_settings()
    engine = get_engine(settings.database_url)
    if engine is None:
        raise RuntimeError("DATABASE_URL is not configured.")
    return read_sql(engine, query)


def load_local_model() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    settings = get_settings()
    fact_sales = pd.read_csv(settings.processed_data_path, parse_dates=["sale_date"])
    dim_product = pd.read_csv(settings.product_dim_path)
    dim_store = pd.read_csv(settings.store_dim_path)
    return fact_sales, dim_product, dim_store


def get_kpi_frame() -> pd.DataFrame:
    return fetch_dataframe(
        """
        SELECT
            ROUND(SUM(revenue), 2) AS total_revenue,
            SUM(quantity) AS total_units,
            ROUND(SUM(revenue) / NULLIF(COUNT(DISTINCT sale_date), 0), 2) AS avg_daily_revenue,
            ROUND(SUM(revenue) / NULLIF(COUNT(*), 0), 2) AS avg_order_value
        FROM fact_sales
        """
    )


def get_daily_trend() -> pd.DataFrame:
    return fetch_dataframe(
        """
        SELECT
            sale_date,
            ROUND(SUM(revenue), 2) AS revenue,
            SUM(quantity) AS units
        FROM fact_sales
        GROUP BY 1
        ORDER BY 1
        """
    )


def get_weekly_trend() -> pd.DataFrame:
    return fetch_dataframe(
        """
        SELECT
            DATE_TRUNC('week', sale_date)::date AS week_start,
            ROUND(SUM(revenue), 2) AS weekly_revenue
        FROM fact_sales
        GROUP BY 1
        ORDER BY 1
        """
    )


def get_product_performance() -> pd.DataFrame:
    return fetch_dataframe(
        """
        SELECT
            p.product_name,
            p.category,
            ROUND(SUM(f.revenue), 2) AS revenue,
            SUM(f.quantity) AS units_sold
        FROM fact_sales f
        JOIN dim_product p ON p.product_id = f.product_id
        GROUP BY 1, 2
        ORDER BY revenue DESC
        """
    )


def get_stock_risk() -> pd.DataFrame:
    return fetch_dataframe(
        """
        WITH latest_stock AS (
            SELECT DISTINCT ON (store_id, product_id)
                store_id,
                product_id,
                stock_on_hand
            FROM fact_sales
            ORDER BY store_id, product_id, sale_date DESC, sale_id DESC
        ),
        recent_demand AS (
            SELECT
                store_id,
                product_id,
                AVG(quantity) AS avg_daily_units
            FROM fact_sales
            WHERE sale_date >= (SELECT MAX(sale_date) FROM fact_sales) - INTERVAL '14 day'
            GROUP BY 1, 2
        )
        SELECT
            s.store_name,
            p.product_name,
            ls.stock_on_hand,
            ROUND(COALESCE(rd.avg_daily_units, 0), 2) AS avg_daily_units,
            ROUND(
                CASE
                    WHEN COALESCE(rd.avg_daily_units, 0) = 0 THEN NULL
                    ELSE ls.stock_on_hand / rd.avg_daily_units
                END,
                1
            ) AS days_left,
            CASE
                WHEN COALESCE(rd.avg_daily_units, 0) = 0 THEN 'Low Movement'
                WHEN ls.stock_on_hand / rd.avg_daily_units < 5 THEN 'High Risk'
                WHEN ls.stock_on_hand / rd.avg_daily_units < 10 THEN 'Watch'
                ELSE 'Healthy'
            END AS risk_status
        FROM latest_stock ls
        JOIN dim_store s ON s.store_id = ls.store_id
        JOIN dim_product p ON p.product_id = ls.product_id
        LEFT JOIN recent_demand rd
            ON rd.store_id = ls.store_id
           AND rd.product_id = ls.product_id
        ORDER BY
            CASE
                WHEN COALESCE(rd.avg_daily_units, 0) = 0 THEN 3
                WHEN ls.stock_on_hand / rd.avg_daily_units < 5 THEN 1
                WHEN ls.stock_on_hand / rd.avg_daily_units < 10 THEN 2
                ELSE 4
            END,
            days_left NULLS LAST
        """
    )


def get_restock_suggestions() -> pd.DataFrame:
    return fetch_dataframe(
        """
        WITH latest_stock AS (
            SELECT DISTINCT ON (store_id, product_id)
                store_id,
                product_id,
                stock_on_hand
            FROM fact_sales
            ORDER BY store_id, product_id, sale_date DESC, sale_id DESC
        ),
        recent_demand AS (
            SELECT
                store_id,
                product_id,
                AVG(quantity) AS avg_daily_units
            FROM fact_sales
            WHERE sale_date >= (SELECT MAX(sale_date) FROM fact_sales) - INTERVAL '14 day'
            GROUP BY 1, 2
        )
        SELECT
            s.store_name,
            p.product_name,
            ROUND(COALESCE(rd.avg_daily_units, 0), 2) AS avg_daily_units,
            ls.stock_on_hand,
            GREATEST(0, CEIL((COALESCE(rd.avg_daily_units, 0) * 14) - ls.stock_on_hand)) AS suggested_reorder_qty
        FROM latest_stock ls
        JOIN dim_store s ON s.store_id = ls.store_id
        JOIN dim_product p ON p.product_id = ls.product_id
        LEFT JOIN recent_demand rd
            ON rd.store_id = ls.store_id
           AND rd.product_id = ls.product_id
        ORDER BY suggested_reorder_qty DESC, avg_daily_units DESC
        """
    )


def get_mix_breakdown() -> tuple[pd.DataFrame, pd.DataFrame]:
    category_mix = fetch_dataframe(
        """
        SELECT
            p.category,
            ROUND(SUM(f.revenue), 2) AS revenue
        FROM fact_sales f
        JOIN dim_product p ON p.product_id = f.product_id
        GROUP BY 1
        ORDER BY revenue DESC
        """
    )
    payment_mix = fetch_dataframe(
        """
        SELECT
            payment_type,
            ROUND(SUM(revenue), 2) AS revenue
        FROM fact_sales
        GROUP BY 1
        ORDER BY revenue DESC
        """
    )
    return category_mix, payment_mix


def get_local_dashboard_frames() -> dict[str, pd.DataFrame | dict[str, float]]:
    fact_sales, dim_product, dim_store = load_local_model()
    fact_sales["revenue"] = fact_sales["revenue"].astype(float)
    fact_sales["quantity"] = fact_sales["quantity"].astype(int)
    fact_sales["stock_on_hand"] = fact_sales["stock_on_hand"].astype(int)

    kpis = {
        "total_revenue": float(fact_sales["revenue"].sum()),
        "total_units": float(fact_sales["quantity"].sum()),
        "avg_daily_revenue": float(fact_sales.groupby("sale_date")["revenue"].sum().mean()),
        "avg_order_value": float(fact_sales["revenue"].mean()),
    }

    daily_trend = (
        fact_sales.groupby("sale_date", as_index=False)
        .agg(revenue=("revenue", "sum"), units=("quantity", "sum"))
        .sort_values("sale_date")
    )

    weekly_trend = (
        fact_sales.assign(week_start=fact_sales["sale_date"].dt.to_period("W-SUN").dt.start_time)
        .groupby("week_start", as_index=False)
        .agg(weekly_revenue=("revenue", "sum"))
        .sort_values("week_start")
    )

    product_perf = (
        fact_sales.merge(dim_product, on="product_id")
        .groupby(["product_name", "category"], as_index=False)
        .agg(revenue=("revenue", "sum"), units_sold=("quantity", "sum"))
        .sort_values("revenue", ascending=False)
    )

    latest_stock = (
        fact_sales.sort_values(["store_id", "product_id", "sale_date", "sale_id"])
        .groupby(["store_id", "product_id"], as_index=False)
        .tail(1)[["store_id", "product_id", "stock_on_hand"]]
    )
    cutoff_date = fact_sales["sale_date"].max() - pd.Timedelta(days=14)
    recent_demand = (
        fact_sales.loc[fact_sales["sale_date"] >= cutoff_date]
        .groupby(["store_id", "product_id"], as_index=False)
        .agg(avg_daily_units=("quantity", "mean"))
    )
    stock_view = (
        latest_stock.merge(recent_demand, on=["store_id", "product_id"], how="left")
        .merge(dim_store, on="store_id")
        .merge(dim_product, on="product_id")
    )
    stock_view["avg_daily_units"] = stock_view["avg_daily_units"].fillna(0.0)
    stock_view["days_left"] = stock_view.apply(
        lambda row: None if row["avg_daily_units"] == 0 else round(row["stock_on_hand"] / row["avg_daily_units"], 1),
        axis=1,
    )
    stock_view["risk_status"] = stock_view.apply(
        lambda row: "Low Movement"
        if row["avg_daily_units"] == 0
        else "High Risk"
        if row["stock_on_hand"] / row["avg_daily_units"] < 5
        else "Watch"
        if row["stock_on_hand"] / row["avg_daily_units"] < 10
        else "Healthy",
        axis=1,
    )
    stock_risk = stock_view[
        ["store_name", "product_name", "stock_on_hand", "avg_daily_units", "days_left", "risk_status"]
    ].sort_values(["risk_status", "days_left"], na_position="last")

    restock = stock_view[
        ["store_name", "product_name", "avg_daily_units", "stock_on_hand"]
    ].copy()
    restock["suggested_reorder_qty"] = (
        (restock["avg_daily_units"] * 14) - restock["stock_on_hand"]
    ).clip(lower=0).apply(lambda value: int(value) if float(value).is_integer() else int(value) + 1)
    restock = restock.sort_values(["suggested_reorder_qty", "avg_daily_units"], ascending=[False, False])

    category_mix = (
        fact_sales.merge(dim_product, on="product_id")
        .groupby("category", as_index=False)
        .agg(revenue=("revenue", "sum"))
        .sort_values("revenue", ascending=False)
    )
    payment_mix = (
        fact_sales.groupby("payment_type", as_index=False)
        .agg(revenue=("revenue", "sum"))
        .sort_values("revenue", ascending=False)
    )

    return {
        "kpis": kpis,
        "daily_trend": daily_trend,
        "weekly_trend": weekly_trend,
        "product_perf": product_perf,
        "stock_risk": stock_risk,
        "restock": restock,
        "category_mix": category_mix,
        "payment_mix": payment_mix,
    }


def build_dashboard() -> None:
    st.set_page_config(page_title="Myanmar Retail Operations Intelligence", layout="wide")
    st.title("Myanmar Retail Operations Intelligence System")
    st.caption("Sales, stock risk, restock suggestions, and weekly trends for a small retail network.")

    use_local_fallback = False

    try:
        kpis = get_kpi_frame().iloc[0]
        daily_trend = get_daily_trend()
        weekly_trend = get_weekly_trend()
        product_perf = get_product_performance()
        stock_risk = get_stock_risk()
        restock = get_restock_suggestions()
        category_mix, payment_mix = get_mix_breakdown()
    except Exception as exc:
        try:
            local_frames = get_local_dashboard_frames()
            kpis = local_frames["kpis"]
            daily_trend = local_frames["daily_trend"]
            weekly_trend = local_frames["weekly_trend"]
            product_perf = local_frames["product_perf"]
            stock_risk = local_frames["stock_risk"]
            restock = local_frames["restock"]
            category_mix = local_frames["category_mix"]
            payment_mix = local_frames["payment_mix"]
            use_local_fallback = True
            st.warning(
                dedent(
                    f"""
                    PostgreSQL is not currently available, so the dashboard is using the local processed CSV files.

                    Connection issue: `{exc}`
                    """
                ).strip()
            )
        except Exception:
            st.error(
                dedent(
                    f"""
                    Dashboard could not connect to PostgreSQL or load local processed files.

                    Reason: `{exc}`

                    Run `python -m src.retail_intel.pipeline` after setting `DATABASE_URL` in `.env`.
                    """
                ).strip()
            )
            return

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue (MMK)", f"{float(kpis['total_revenue']):,.0f}")
    col2.metric("Units Sold", f"{int(float(kpis['total_units'])):,}")
    col3.metric("Avg Daily Revenue", f"{float(kpis['avg_daily_revenue']):,.0f}")
    col4.metric("Avg Order Value", f"{float(kpis['avg_order_value']):,.0f}")

    left, right = st.columns(2)
    with left:
        st.subheader("Daily Revenue Trend")
        st.line_chart(daily_trend.set_index("sale_date")["revenue"])
    with right:
        st.subheader("Weekly Revenue Trend")
        st.bar_chart(weekly_trend.set_index("week_start")["weekly_revenue"])

    left, right = st.columns(2)
    with left:
        st.subheader("Top Product Performance")
        st.dataframe(product_perf.head(10), use_container_width=True, hide_index=True)
    with right:
        st.subheader("Stock Risk")
        st.dataframe(stock_risk.head(15), use_container_width=True, hide_index=True)

    left, right = st.columns(2)
    with left:
        st.subheader("Restock Suggestions")
        st.dataframe(restock.head(15), use_container_width=True, hide_index=True)
    with right:
        st.subheader("Payment Mix")
        st.dataframe(payment_mix, use_container_width=True, hide_index=True)

    st.subheader("Category Mix")
    st.dataframe(category_mix, use_container_width=True, hide_index=True)

    if use_local_fallback:
        st.caption("Dashboard mode: local CSV fallback. SQL-backed metrics become active once PostgreSQL is connected.")
