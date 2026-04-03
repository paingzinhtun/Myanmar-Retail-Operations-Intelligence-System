# Data Modeling Learning Path

This folder is a practical learning track for understanding data modeling with the Myanmar Retail Operations Intelligence System.

It is built to help you do two things:

- learn data modeling in a structured way
- explain data modeling to other people using this project as the example

## Why this matters

Data modeling is how we turn real business activity into data structures that are clear, consistent, and useful.

In this project, that means turning retail reality into tables, keys, relationships, and business events that support analytics.

If you learn this well, you will be able to:

- design better tables before writing SQL
- understand why some reports are easy and others are painful
- make your project easier to grow later
- explain your system like a data engineer, analytics engineer, or BI developer

## Recommended learning order

1. [01-foundations.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\01-foundations.md)
2. [02-project-reality-map.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\02-project-reality-map.md)
3. [03-star-schema-and-grain.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\03-star-schema-and-grain.md)
4. [04-future-proof-modeling.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\04-future-proof-modeling.md)
5. [05-learning-roadmap.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\05-learning-roadmap.md)

## Myanmar version

Myanmar-language versions of the same guides are available here:

1. [README-mm.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\README-mm.md)
2. [01-foundations-mm.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\01-foundations-mm.md)
3. [02-project-reality-map-mm.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\02-project-reality-map-mm.md)
4. [03-star-schema-and-grain-mm.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\03-star-schema-and-grain-mm.md)
5. [04-future-proof-modeling-mm.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\04-future-proof-modeling-mm.md)
6. [05-learning-roadmap-mm.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\05-learning-roadmap-mm.md)

## How to use this folder

- Read the files in order if you are learning for yourself.
- Share individual files if you are teaching one topic at a time.
- Use the examples to compare the current schema with a stronger future design.
- Revisit the roadmap when you want to extend the project.

## Current project anchor points

These project files are the main references for the lessons:

- [sql/schema.sql](c:\Users\HP\Desktop\Myn_retail\sql\schema.sql)
- [src/retail_intel/pipeline.py](c:\Users\HP\Desktop\Myn_retail\src\retail_intel\pipeline.py)
- [src/retail_intel/data_generator.py](c:\Users\HP\Desktop\Myn_retail\src\retail_intel\data_generator.py)
- [sql/metrics.sql](c:\Users\HP\Desktop\Myn_retail\sql\metrics.sql)

## Big picture

The current project already has a useful analytics model:

- `dim_product`
- `dim_store`
- `fact_sales`

That is a strong starting point.

The deeper learning path is understanding:

- what reality is being represented
- what has been simplified
- what could be added later without breaking the design

That is where data modeling becomes future-proof.
