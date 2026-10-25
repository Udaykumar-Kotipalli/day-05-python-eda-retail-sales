# Day 5 — Python Exploratory Data Analysis (EDA): Retail Sales

A reproducible exploratory data analysis project using **Python, Pandas, Matplotlib, and Seaborn** to explore sales trends, product categories, city performance, and payment methods.

> **Data notice:** All 1,200 records are synthetic and generated for portfolio practice. They do not represent a real company or actual customer transactions.

## Objectives
- Calculate retail KPIs and summary statistics.
- Explore monthly net sales trends.
- Compare product category and city performance.
- Examine payment method usage.
- Export summary tables, metrics, and charts.

## Repository structure
```text
day-05-python-eda-retail-sales/
├── data/retail_sales.csv
├── notebooks/retail_sales_eda.ipynb
├── outputs/
│   ├── charts/
│   │   ├── monthly_sales_trend.png
│   │   ├── sales_by_category.png
│   │   ├── sales_by_city.png
│   │   └── payment_method_mix.png
│   ├── eda_summary.json
│   ├── monthly_sales.csv
│   ├── sales_by_category.csv
│   └── sales_by_city.csv
├── src/run_eda.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Dataset
The CSV contains 1,200 synthetic order records dated in 2025.

| Column | Description |
|---|---|
| `order_id` | Unique synthetic order identifier |
| `order_date` | Order date |
| `city` | City associated with the order |
| `category` | Product category |
| `product` | Product name |
| `quantity` | Units ordered |
| `unit_price_inr` | Unit price in INR |
| `discount_pct` | Discount rate |
| `gross_sales_inr` | Quantity × unit price |
| `net_sales_inr` | Sales after discount |
| `payment_method` | Payment method category |

## Setup and run
Run from the repository root.

```bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install packages and run:

```bash
python -m pip install -r requirements.txt
python src/run_eda.py
```

The script writes summary JSON, grouped CSV files, and charts into `outputs/`.

## Business questions
1. How does net sales change month by month?
2. Which product category contributes the most net sales?
3. Which city contributes the most net sales?
4. Which payment method is used for the most orders?
5. Which KPIs could a retail manager review regularly?

## Methodology
1. Load the CSV and parse dates with Pandas.
2. Derive a month field for trend analysis.
3. Calculate KPIs and grouped summaries.
4. Visualize trends and comparisons with Matplotlib and Seaborn.
5. Export results for reproducible review.

## Outputs
- `eda_summary.json`: core KPIs and top-performing dimensions.
- `monthly_sales.csv`: monthly sales summary.
- `sales_by_category.csv`: category-level summary.
- `sales_by_city.csv`: city-level summary.
- `outputs/charts/`: four generated visualizations.

## Limitations
- Synthetic data is not suitable for real-world market conclusions.
- The dataset does not model all retail factors, such as returns, taxes, inventory constraints, or customer-level behavior.
- Patterns are illustrative and should not be treated as evidence of actual business performance.

## Skills demonstrated
Python · Pandas · Exploratory data analysis · KPI calculation · Data aggregation · Matplotlib · Seaborn · CSV/JSON exports · Business insight communication
