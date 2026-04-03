# 02 Project Reality Map

## What reality this project currently models

This project models a retail analytics scenario, not a full POS or ERP system.

The current schema in [sql/schema.sql](c:\Users\HP\Desktop\Myn_retail\sql\schema.sql) is focused on sales analysis:

- `dim_product`
- `dim_store`
- `fact_sales`

That means the project is modeling:

- which products exist
- which stores exist
- which sales happened

## Current entities

### Product

Represented by `dim_product`.

Attributes:

- `product_id`
- `product_name`
- `category`
- `supplier`
- `default_unit_price`

Business meaning:

- a product is something the business sells
- category and supplier describe the product
- the default unit price is a reference value, not always the actual selling price

### Store

Represented by `dim_store`.

Attributes:

- `store_id`
- `store_name`
- `city`
- `township`

Business meaning:

- a store is a place where sales happen
- city and township describe location

## Current event

### Sale

Represented by `fact_sales`.

Attributes:

- `sale_id`
- `sale_date`
- `product_id`
- `store_id`
- `quantity`
- `unit_price`
- `revenue`
- `stock_on_hand`
- `payment_type`

Business meaning:

- one row describes a recorded sales event for a product at a store on a date

This is the core measurable activity in the project.

## Current relationships

The current model expresses these relationships:

- one product can appear in many sales
- one store can appear in many sales
- each sale belongs to one product
- each sale belongs to one store

You can describe it like this:

```text
dim_product 1 -> many fact_sales
dim_store   1 -> many fact_sales
```

## How raw data becomes modeled data

The generator in [src/retail_intel/data_generator.py](c:\Users\HP\Desktop\Myn_retail\src\retail_intel\data_generator.py) creates retail-like rows with product names, store names, quantities, prices, stock levels, and payment types.

The pipeline in [src/retail_intel/pipeline.py](c:\Users\HP\Desktop\Myn_retail\src\retail_intel\pipeline.py) then:

- cleans those values
- separates descriptive data into dimensions
- maps business activity into the fact table

This is a classic example of moving from messy business records to analytics-friendly structure.

## What is simplified right now

The project is intentionally simplified.

It does not currently model:

- customer
- order
- order item
- payment as its own table
- supplier as its own dimension
- inventory movements as separate events

That is okay for the current goal because the project is solving analytics questions, not full transaction processing.

## Why this is still impactful

Yes, this project is absolutely useful for learning data modeling.

It is impactful because it teaches a very important truth:

- you do not need to model everything at once
- you need to model enough reality to answer real questions well

This project already answers questions like:

- what did we sell
- where did we sell it
- which products drive revenue
- where is stock risk increasing

That is real modeling value.
