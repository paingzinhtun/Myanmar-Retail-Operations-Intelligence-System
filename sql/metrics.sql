WITH daily_sales AS (
    SELECT
        f.sale_date,
        s.store_name,
        SUM(f.revenue) AS daily_revenue,
        SUM(f.quantity) AS units_sold
    FROM fact_sales f
    JOIN dim_store s ON s.store_id = f.store_id
    GROUP BY 1, 2
)
SELECT *
FROM daily_sales
ORDER BY sale_date DESC, store_name;


WITH weekly_sales AS (
    SELECT
        DATE_TRUNC('week', sale_date)::date AS week_start,
        SUM(revenue) AS weekly_revenue
    FROM fact_sales
    GROUP BY 1
)
SELECT
    week_start,
    weekly_revenue,
    weekly_revenue - LAG(weekly_revenue) OVER (ORDER BY week_start) AS revenue_change
FROM weekly_sales
ORDER BY week_start DESC;


WITH product_performance AS (
    SELECT
        p.product_name,
        p.category,
        SUM(f.quantity) AS total_units,
        SUM(f.revenue) AS total_revenue
    FROM fact_sales f
    JOIN dim_product p ON p.product_id = f.product_id
    GROUP BY 1, 2
)
SELECT *
FROM product_performance
ORDER BY total_revenue DESC;


WITH latest_stock AS (
    SELECT DISTINCT ON (store_id, product_id)
        store_id,
        product_id,
        stock_on_hand,
        sale_date
    FROM fact_sales
    ORDER BY store_id, product_id, sale_date DESC, sale_id DESC
),
recent_demand AS (
    SELECT
        store_id,
        product_id,
        AVG(quantity) AS avg_daily_units_last_14_days
    FROM fact_sales
    WHERE sale_date >= CURRENT_DATE - INTERVAL '14 day'
    GROUP BY 1, 2
)
SELECT
    s.store_name,
    p.product_name,
    ls.stock_on_hand,
    COALESCE(rd.avg_daily_units_last_14_days, 0) AS avg_daily_units_last_14_days,
    CASE
        WHEN COALESCE(rd.avg_daily_units_last_14_days, 0) = 0 THEN NULL
        ELSE ROUND(ls.stock_on_hand / rd.avg_daily_units_last_14_days, 1)
    END AS estimated_days_left,
    GREATEST(0, CEIL((COALESCE(rd.avg_daily_units_last_14_days, 0) * 14) - ls.stock_on_hand)) AS suggested_reorder_qty
FROM latest_stock ls
JOIN dim_store s ON s.store_id = ls.store_id
JOIN dim_product p ON p.product_id = ls.product_id
LEFT JOIN recent_demand rd
    ON rd.store_id = ls.store_id
   AND rd.product_id = ls.product_id
ORDER BY suggested_reorder_qty DESC, estimated_days_left NULLS LAST;
