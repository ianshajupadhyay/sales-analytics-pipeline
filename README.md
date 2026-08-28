# Olist Sales Analytics Pipeline

## Overview

An end-to-end Analytics Engineering project using the Brazilian Olist e-commerce dataset.

The project demonstrates how raw e-commerce data can be ingested, transformed, tested and converted into business-ready analytical data marts for BI consumption.

## Objective

The goal of this project was to understand the complete Analytics Engineering workflow:

**Raw Data → Python → PostgreSQL → dbt → Data Marts → BI**

Key areas covered:

- Data ingestion using Python
- PostgreSQL data storage
- SQL transformations
- dbt staging, intermediate and mart layers
- Dimensional data modeling
- Data quality testing
- Pipeline logging
- BI consumption using Tableau
- Git/GitHub project management

## Architecture

Olist Dataset
      ↓
Python Ingestion
      ↓
PostgreSQL
      ↓
dbt
 ┌────┼──────────┐
 ↓    ↓          ↓
Staging → Intermediate → Marts
                         ↓
                    BI / Tableau


## Technology Stack

| Area | Technology |
|---|---|
| Language | Python / SQL |
| Database | PostgreSQL |
| Transformation | dbt |
| Testing | dbt tests |
| BI | Tableau |
| Version Control | Git / GitHub |

## Data Modeling

The dbt project follows a layered transformation approach:

Raw
 ↓
Staging
 ↓
Intermediate
 ↓
Marts


### Key Data Marts

- `fct_orders` - order-level analysis
- `fct_order_items` - order-item level analysis
- `fct_payments` - payment analysis
- `fct_reviews` - review analysis
- `dim_customer` - customer attributes
- `dim_product` - product attributes
- `dim_seller` - seller attributes
- `dim_date` - calendar and time analysis

The models maintain appropriate grain between orders, order items, payments and reviews to support reliable analytical queries and avoid double counting.

## Data Quality & Logging

The project includes dbt tests covering areas such as:

- Primary key uniqueness
- Not-null validation
- Referential integrity
- Model-level data quality

Logging is implemented within the ingestion/pipeline process to provide visibility into successful execution and failures.

## Tableau

A Tableau Executive Summary was created as the BI consumption layer.

The dashboard provides a high-level view of sales and order performance and demonstrates how the analytical marts can be consumed by a BI tool.

The Tableau workbook is located in:

tableau/

Advanced Tableau development is outside the primary scope of this project, as the main objective was to understand the end-to-end Analytics Engineering workflow.

## Running the Project

### 1. Activate the environment

```bash
source .venv/bin/activate
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Python ingestion process

Run the project's ingestion script to load the Olist data into PostgreSQL.

### 4. Run dbt

```bash
cd analytics_dbt

dbt debug
dbt deps
dbt run
dbt test
```

## Project Structure

```text
sales-analytics-pipeline/
│
├── analytics_dbt/
│   ├── dbt_project.yml
│   ├── models/
│   │   ├── staging/
│   │   ├── intermediate/
│   │   └── marts/
│   └── dbt_packages/
│
├── tableau/
│   └── sales_analytics.twb
│
├── Python / ingestion
├── SQL
├── logs
├── requirements.txt
├── .gitignore
└── README.md
```

## Project Status

**Completed**

The project demonstrates an end-to-end Analytics Engineering workflow using Olist data, from ingestion and PostgreSQL storage through dbt transformation, data modeling, testing, logging, analytical marts and BI consumption.

**Sales Analytics Project — Complete**