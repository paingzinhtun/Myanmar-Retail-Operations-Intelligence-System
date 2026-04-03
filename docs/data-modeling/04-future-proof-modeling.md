# 04 Future Proof Modeling

## What future-proof means

Future-proof modeling does not mean predicting everything.

It means designing in a way that lets the project grow without forcing a painful rebuild later.

For this retail project, that means preparing for deeper business reality while keeping the current analytics model useful.

## The next likely expansion areas

If this project grows, these are the most natural additions:

- customer data
- order headers
- order line items
- payment events
- inventory movement events
- supplier dimension
- time dimension

## A stronger future retail model

Here is a practical target design:

```text
dim_customer
dim_product
dim_store
dim_supplier
dim_date

fact_order
fact_order_item
fact_payment
fact_inventory_movement
```

## Why separate these concepts

### Customer

Add `dim_customer` when you want to answer:

- who buys most often
- repeat purchase behavior
- customer lifetime value

### Order and order item

Split orders into header and line-item concepts when one order can contain multiple products.

That allows:

- basket analysis
- average order value by actual order
- promotions across multiple items

### Payment as its own event

Keep payment separate when:

- one order can have multiple payment attempts
- refunds can happen
- payment status matters

### Inventory movement

Stock on hand is useful, but inventory movement events are deeper and more reliable.

Examples:

- goods received
- transfer in
- transfer out
- adjustment
- sale deduction
- return to stock

This helps when inventory becomes a serious business function.

## Design principles that age well

### Keep business meaning clear

Every table should answer:

- what does one row mean
- why does this table exist

### Prefer stable surrogate keys in analytics models

Examples:

- `product_id`
- `store_id`
- `customer_id`

This protects joins even if labels change.

### Separate descriptive data from event data

Avoid stuffing all product and store details directly into every event row if you want a cleaner analytics model.

### Model time carefully

Time is one of the biggest growth areas in data systems.

Think about:

- event time
- load time
- update time
- business effective dates

### Expect change

Future-proof models assume:

- prices may change
- products may be renamed
- stores may move
- customers may merge or split
- payments may fail and retry

Your model should not break when reality becomes more realistic.

## What to improve in this project over time

A realistic evolution path would be:

1. Add `dim_customer`
2. Replace simple sales rows with `fact_order` and `fact_order_item`
3. Move `payment_type` into a payment event model
4. Add supplier and inventory movement tables
5. Introduce a time dimension if reporting becomes more advanced

That path keeps the current work valuable while making the model more mature.

## The most important future-proof habit

Write down the grain and business definition of every table in words before implementing it.

That one practice prevents many design problems.
