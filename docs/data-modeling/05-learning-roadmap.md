# 05 Learning Roadmap

## Your starting point

Yes, this project is a strong place to start learning data modeling in depth.

It is especially useful because it already contains:

- raw business-like data
- a cleaning pipeline
- dimension and fact modeling
- SQL analytics
- business questions tied to the model

That makes it much better than learning from isolated theory alone.

## Stage 1: Learn the language

Focus on these ideas first:

- entity
- event
- relationship
- key
- fact table
- dimension table
- grain

Your goal:

- explain each term in your own words using this project

Practice:

- describe `dim_product`, `dim_store`, and `fact_sales` out loud
- write one sentence for the grain of `fact_sales`

## Stage 2: Learn to read the current model

Study these files:

- [sql/schema.sql](c:\Users\HP\Desktop\Myn_retail\sql\schema.sql)
- [src/retail_intel/pipeline.py](c:\Users\HP\Desktop\Myn_retail\src\retail_intel\pipeline.py)
- [sql/metrics.sql](c:\Users\HP\Desktop\Myn_retail\sql\metrics.sql)

Your goal:

- understand why the current model answers retail analytics questions well

Practice:

- trace one raw row from generation to cleaned data to fact table
- explain how joins connect `fact_sales` to `dim_product` and `dim_store`

## Stage 3: Learn design tradeoffs

Now ask deeper questions:

- why is `payment_type` inside `fact_sales` instead of a payment table
- why is supplier inside `dim_product` instead of `dim_supplier`
- why is stock represented as a value, not a movement event

Your goal:

- understand that models are choices, not just definitions

Practice:

- list three strengths of the current design
- list three limitations if the system becomes more realistic

## Stage 4: Extend the model

Start sketching the future version:

- `dim_customer`
- `fact_order`
- `fact_order_item`
- `fact_payment`

Your goal:

- learn how modeling grows with business needs

Practice:

- define the grain for each new table
- write the primary key and foreign keys you would use
- list the business questions each table enables

## Stage 5: Teach it

The best way to deepen your understanding is to teach it.

Use this project to explain:

- how data represents reality
- why star schemas are useful
- how grain affects reports
- how to grow from a simple analytics model to a richer retail model

Your goal:

- be able to explain the project from both beginner and practical business perspectives

## A shareable teaching outline

You can teach this project in five short sessions:

1. What is data modeling
2. Entities, events, and relationships in retail
3. Why this project uses dimension and fact tables
4. What grain means and why it matters
5. How to make the model future-proof

## Recommended next project tasks

When you are ready to go beyond theory, build one of these:

1. Add a `dim_customer` table and explain why it is an entity
2. Create a draft `fact_order_item` schema and define its grain
3. Add a document comparing the current model with a fuller order-based model
4. Build one new SQL metric that depends on a richer model design

## Final advice

Do not rush to make the model complex.

First learn to explain:

- what reality is being modeled now
- why that current model works
- where it will break as reality becomes deeper

That is the path from beginner understanding to strong modeling judgment.
