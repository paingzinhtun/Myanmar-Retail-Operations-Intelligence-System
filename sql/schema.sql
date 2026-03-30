CREATE TABLE IF NOT EXISTS dim_product (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL UNIQUE,
    category TEXT NOT NULL,
    supplier TEXT NOT NULL,
    default_unit_price NUMERIC(14, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_store (
    store_id INTEGER PRIMARY KEY,
    store_name TEXT NOT NULL UNIQUE,
    city TEXT NOT NULL,
    township TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_sales (
    sale_id BIGINT PRIMARY KEY,
    sale_date DATE NOT NULL,
    product_id INTEGER NOT NULL REFERENCES dim_product(product_id),
    store_id INTEGER NOT NULL REFERENCES dim_store(store_id),
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(14, 2) NOT NULL,
    revenue NUMERIC(14, 2) NOT NULL,
    stock_on_hand INTEGER NOT NULL,
    payment_type TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_fact_sales_date ON fact_sales (sale_date);
CREATE INDEX IF NOT EXISTS idx_fact_sales_product_date ON fact_sales (product_id, sale_date);
CREATE INDEX IF NOT EXISTS idx_fact_sales_store_date ON fact_sales (store_id, sale_date);
