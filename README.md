# Myanmar Retail Operations Intelligence System

### Turn daily shop data into sales insight, stock warnings, and smarter restock decisions.

An end-to-end retail analytics project built for Myanmar shop and distributor use cases. It simulates realistic retail transactions, cleans and models the data, loads it into PostgreSQL, and presents business-ready insights in a Streamlit dashboard.

This project is designed to be useful in two ways:

- for beginners, it shows the full data workflow from raw data to dashboard
- for intermediate and advanced learners, it demonstrates practical analytics engineering, KPI design, SQL reporting, and automation

## Why This Project Matters

Small retail businesses do not just need charts. They need answers to questions like:

- How much did we sell today?
- Which products are driving revenue?
- Which items are close to stockout?
- What should we restock this week?
- Is business growing or slowing down?

This system is built around those business questions. That makes it more than a coding exercise. It is a portfolio project with real service potential for local shops, mini marts, and small distributors.

## Project Highlights

- simulated Myanmar retail sales data with local stores, products, suppliers, and payment types
- cleaning pipeline using Pandas
- star-style retail data model with dimensions and fact table
- PostgreSQL storage and SQL analytics queries
- Streamlit dashboard for business reporting
- automated refresh with APScheduler
- Windows Task Scheduler setup for local automation

## What You Will Learn

This single project helps you practice:

- `ingestion`: generating and capturing raw business events
- `cleaning`: standardizing messy fields and fixing data quality issues
- `modeling`: converting raw records into dimension and fact tables
- `analytics`: building KPIs, trends, product performance, and stock intelligence
- `business thinking`: measuring what actually matters to a retailer
- `reporting`: presenting results in a dashboard decision-makers can understand
- `automation`: refreshing data on a schedule
- `local problem understanding`: using Myanmar-style retail context, MMK pricing, and local payment methods

## Business Questions Answered

The dashboard and SQL layer are built to answer these questions:

- What is the total revenue today, this week, and over time?
- Which products generate the most revenue and units sold?
- Which categories are performing best?
- Which stores are strongest or weakest?
- Which items are at high stock risk?
- What reorder quantity should we suggest based on recent demand?
- What payment methods are customers using most?

## Architecture

```text
Simulated Retail Transactions
        ->
Raw CSV
        ->
Cleaning + Validation with Pandas
        ->
dim_product + dim_store + fact_sales
        ->
PostgreSQL
        ->
SQL Metrics + Streamlit Dashboard
        ->
Scheduled Refresh
```

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQL
- Streamlit
- SQLAlchemy
- APScheduler
- Git and GitHub

## Project Structure

```text
.
|-- app.py
|-- requirements.txt
|-- .env.example
|-- sql/
|   |-- schema.sql
|   `-- metrics.sql
|-- data/
|   |-- raw/
|   `-- processed/
`-- src/
    `-- retail_intel/
        |-- config.py
        |-- data_generator.py
        |-- db.py
        |-- metrics.py
        |-- pipeline.py
        `-- scheduler.py
```

## End-to-End Flow

### 1. Ingestion

Raw retail sales are simulated in [data_generator.py](/Users/HP/Desktop/Myn_retail/src/retail_intel/data_generator.py). The generator creates transactions across Myanmar-style stores, products, suppliers, and payment types, then writes the results to `data/raw/retail_sales_raw.csv`.

### 2. Cleaning

The cleaning logic lives in [pipeline.py](/Users/HP/Desktop/Myn_retail/src/retail_intel/pipeline.py). It:

- standardizes text values
- converts date and numeric columns
- removes duplicates
- clips invalid negative values
- creates revenue fields needed for analysis

### 3. Modeling

The pipeline transforms raw data into:

- `dim_product`
- `dim_store`
- `fact_sales`

This creates an analytics-friendly structure that is easy to query and visualize.

### 4. Analytics

SQL and Python metrics calculate:

- daily revenue
- weekly revenue trend
- product performance
- stock risk
- restock suggestions
- category mix
- payment mix

See [schema.sql](/Users/HP/Desktop/Myn_retail/sql/schema.sql) and [metrics.sql](/Users/HP/Desktop/Myn_retail/sql/metrics.sql).

### 5. Reporting

The Streamlit app presents the metrics in a business-friendly dashboard through [app.py](/Users/HP/Desktop/Myn_retail/app.py) and [metrics.py](/Users/HP/Desktop/Myn_retail/src/retail_intel/metrics.py).

### 6. Automation

The refresh process can run on a schedule using [scheduler.py](/Users/HP/Desktop/Myn_retail/src/retail_intel/scheduler.py) or Windows Task Scheduler.

## Dashboard Features

- KPI cards for revenue, units sold, average daily revenue, and average order value
- daily revenue line chart
- weekly revenue trend chart
- top product performance table
- stock risk table
- restock suggestion table
- category mix summary
- payment mix summary

## Dashboard Preview

Add a Streamlit dashboard screenshot at:

`assets/streamlit-dashboard.png`

Then GitHub will render it here:

![Myanmar Retail Streamlit Dashboard](assets/streamlit-dashboard.png)

## Data Model

### `dim_product`

- product identifier
- product name
- category
- supplier
- default unit price

### `dim_store`

- store identifier
- store name
- city
- township

### `fact_sales`

- sale identifier
- sale date
- product identifier
- store identifier
- quantity
- unit price
- revenue
- stock on hand
- payment type

## Quick Start

### 1. Open the project folder

```powershell
cd c:\Users\HP\Desktop\Myn_retail
```

### 2. Create a virtual environment

```powershell
py -3 -m venv .venv
```

### 3. Activate it

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Create `.env`

Copy from `.env.example` and set your PostgreSQL connection:

```env
DATABASE_URL=postgresql+psycopg2://postgres:yourpassword@localhost:5432/myanmar_retail
RAW_DATA_PATH=data/raw/retail_sales_raw.csv
PROCESSED_DATA_PATH=data/processed/fact_sales.csv
DAYS_OF_HISTORY=120
RANDOM_SEED=42
REFRESH_MODE=daily
REFRESH_INTERVAL_MINUTES=5
REFRESH_HOUR=6
REFRESH_MINUTE=0
```

### 6. Make sure PostgreSQL is running

Create the database if needed:

```sql
CREATE DATABASE myanmar_retail;
```

### 7. Run the pipeline

```powershell
py -3 -m src.retail_intel.pipeline
```

If the load works, the printed result should include:

```text
'db_loaded': True
```

### 8. Launch the dashboard

```powershell
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

## Refresh Modes

### Demo mode: every few minutes

Use this in `.env`:

```env
REFRESH_MODE=interval
REFRESH_INTERVAL_MINUTES=5
```

Run:

```powershell
py -3 -m src.retail_intel.scheduler
```

### Daily mode

Use this in `.env`:

```env
REFRESH_MODE=daily
REFRESH_HOUR=6
REFRESH_MINUTE=0
```

Run:

```powershell
py -3 -m src.retail_intel.scheduler
```

## Windows Task Scheduler Setup

If you want automatic refresh without keeping a terminal open:

1. Open `Task Scheduler`
2. Click `Create Task`
3. Name it `Myanmar Retail Daily Refresh`
4. Add a `Daily` trigger
5. Add an action with:

```text
Program/script: py
Add arguments: -3 -m src.retail_intel.pipeline
Start in: c:\Users\HP\Desktop\Myn_retail
```

6. Save the task
7. Run it once manually to confirm that the CSV files and database tables update

For demo mode, you can configure the trigger to repeat every `5 minutes`.

## Fallback Behavior

If PostgreSQL is not available, the project still writes processed CSV files locally. The dashboard can read those files as a fallback so the demo remains usable.

## Why This README Is Good For Portfolio Use

If you put this on GitHub, it tells a strong story:

- you can build data pipelines, not just notebooks
- you understand business metrics, not just code
- you can model data for analytics
- you can build dashboards for non-technical users
- you can automate workflows
- you can frame a technical project around a real local problem

## Future Improvements

- connect to real POS or spreadsheet data instead of simulation
- add supplier lead time and more advanced reorder logic
- support multiple distributors and branches
- add profit margin and gross profit analytics
- add alerts for high stock risk products
- deploy the Streamlit app to cloud hosting

## Author Pitch

This project shows how data engineering, analytics, and business understanding can come together in a practical retail solution. It starts simple enough for a beginner to follow, but the design is strong enough to grow into a real client-facing product.
