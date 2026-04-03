# 03 Star Schema And Grain

## Why this project uses a star-style model

The current design is an analytics model, so it uses dimensions and a fact table.

That pattern is often called a star schema.

In simple terms:

- dimensions describe business entities
- fact tables record measurable events

For this project:

- `dim_product` is a dimension
- `dim_store` is a dimension
- `fact_sales` is a fact table

## Why this is good for analytics

This structure makes it easier to ask:

- revenue by day
- revenue by store
- revenue by product
- units sold by category
- stock risk by product and store

This is exactly what [sql/metrics.sql](c:\Users\HP\Desktop\Myn_retail\sql\metrics.sql) is doing.

## The most important concept: grain

Grain means the exact business meaning of one row in a table.

If the grain is unclear, the model becomes confusing and metrics become unreliable.

For `fact_sales`, the current grain is approximately:

`one recorded product sale at one store on one date for one sale record`

That definition explains why the table can support product-level and store-level reporting.

## Why grain matters

Grain controls:

- what can be summed safely
- what can be joined safely
- what counts as a duplicate
- what questions the table can answer

If you mix multiple grains in one table, reports start lying.

Examples of grain mistakes:

- putting order-level and item-level fields in one row without a clear rule
- storing both daily summaries and raw transactions in the same fact table
- joining dimensions in ways that duplicate facts

## Dimension table mindset

Dimension tables usually contain:

- identifiers
- labels
- categories
- descriptive attributes

In this project:

- product name, category, supplier are descriptive
- store name, city, township are descriptive

These are useful for filtering, grouping, and labeling reports.

## Fact table mindset

Fact tables usually contain:

- foreign keys to dimensions
- dates or timestamps
- measurable numeric values

In this project:

- `product_id` and `store_id` link to dimensions
- `sale_date` tells when the event happened
- `quantity`, `unit_price`, and `revenue` are measures

## Key lesson

When designing analytics models, start with the event and its grain first.

Ask:

1. What event are we measuring?
2. What does one row mean?
3. Which dimensions describe that event?
4. Which measures belong at that same level?

That sequence is safer than starting with columns.
