# 01 Foundations

## What is data modeling

Data modeling is the practice of deciding how real-world things, actions, and rules should be represented in data.

A good model is not just a set of tables. It is a clear explanation of reality:

- what exists
- what happens
- what connects
- what can change over time

## The three core ideas

### 1. Entity

An entity is a thing that exists and can be identified.

Examples:

- customer
- product
- store
- supplier
- order

Questions to ask:

- Does this thing exist independently?
- Do we need to identify it repeatedly over time?
- Does it have attributes we want to describe?

### 2. Event

An event is something that happens at a point in time.

Examples:

- order placed
- sale completed
- payment made
- stock replenished
- item returned

Questions to ask:

- Did something happen?
- When did it happen?
- Can it happen many times?
- Do we want to measure it?

### 3. Relationship

A relationship is how entities and events connect.

Examples:

- customer places orders
- order contains products
- store records sales
- supplier provides products

Questions to ask:

- Which things are connected?
- Is the connection one-to-one, one-to-many, or many-to-many?
- Does the relationship itself need attributes?

## How data represents reality

Think of business reality as three layers:

1. Stable things
2. Business actions
3. Rules about how they connect

In a retail system:

- product is a stable thing
- customer is a stable thing
- order placed is a business action
- customer to order is a relationship

That becomes a model like this:

```text
Customer -> Order -> Order Item -> Product
                  -> Payment
```

## What makes a model good

A good data model is:

- understandable
- consistent
- queryable
- extensible
- aligned with business questions

A weak model usually has these problems:

- mixed meanings in one table
- missing keys
- duplicated logic
- unclear time behavior
- tables designed only for one report

## Important habit

Before creating a table, ask:

1. Is this an entity, an event, or a relationship?
2. What is the business meaning of one row?
3. What is the unique identifier?
4. What changes over time?
5. What questions should this model answer later?

If you make this a habit, your designs will become much stronger.
