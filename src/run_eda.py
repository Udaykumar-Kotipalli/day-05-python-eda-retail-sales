from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "retail_sales.csv"
OUTPUT_DIR = ROOT / "outputs"
CHART_DIR = OUTPUT_DIR / "charts"
OUTPUT_DIR.mkdir(exist_ok=True)
CHART_DIR.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(DATA_PATH, parse_dates=["order_date"])
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    metrics = {
        "dataset_rows": int(len(df)),
        "date_range_start": str(df["order_date"].min().date()),
        "date_range_end": str(df["order_date"].max().date()),
        "total_orders": int(df["order_id"].nunique()),
        "total_units": int(df["quantity"].sum()),
        "gross_sales_inr": round(float(df["gross_sales_inr"].sum()), 2),
        "net_sales_inr": round(float(df["net_sales_inr"].sum()), 2),
        "average_order_value_inr": round(float(df.groupby("order_id")["net_sales_inr"].sum().mean()), 2),
        "top_category_by_net_sales": str(df.groupby("category")["net_sales_inr"].sum().idxmax()),
        "top_city_by_net_sales": str(df.groupby("city")["net_sales_inr"].sum().idxmax()),
        "top_payment_method_by_orders": str(df["payment_method"].value_counts().idxmax()),
    }
    (OUTPUT_DIR / "eda_summary.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    df.groupby("category", as_index=False).agg(orders=("order_id","nunique"), units=("quantity","sum"), net_sales_inr=("net_sales_inr","sum")).sort_values("net_sales_inr",ascending=False).to_csv(OUTPUT_DIR/"sales_by_category.csv",index=False)
    df.groupby("city", as_index=False).agg(orders=("order_id","nunique"), units=("quantity","sum"), net_sales_inr=("net_sales_inr","sum")).sort_values("net_sales_inr",ascending=False).to_csv(OUTPUT_DIR/"sales_by_city.csv",index=False)
    df.groupby("month", as_index=False).agg(orders=("order_id","nunique"), net_sales_inr=("net_sales_inr","sum")).to_csv(OUTPUT_DIR/"monthly_sales.csv",index=False)
    sns.set_theme(style="whitegrid")
    monthly=df.groupby("month",as_index=False)["net_sales_inr"].sum()
    fig,ax=plt.subplots(figsize=(11,5)); ax.plot(monthly["month"], monthly["net_sales_inr"], marker="o")
    ax.set(title="Monthly Net Sales Trend (Synthetic Retail Data)",xlabel="Month",ylabel="Net sales (INR)")
    ax.tick_params(axis="x",rotation=45); fig.tight_layout(); fig.savefig(CHART_DIR/"monthly_sales_trend.png",dpi=160); plt.close(fig)
    category=df.groupby("category",as_index=False)["net_sales_inr"].sum().sort_values("net_sales_inr",ascending=False)
    fig,ax=plt.subplots(figsize=(9,5)); ax.bar(category["category"], category["net_sales_inr"])
    ax.set(title="Net Sales by Product Category",xlabel="Category",ylabel="Net sales (INR)")
    ax.tick_params(axis="x",rotation=20); fig.tight_layout(); fig.savefig(CHART_DIR/"sales_by_category.png",dpi=160); plt.close(fig)
    city=df.groupby("city",as_index=False)["net_sales_inr"].sum().sort_values("net_sales_inr",ascending=False)
    fig,ax=plt.subplots(figsize=(9,5)); ax.bar(city["city"], city["net_sales_inr"])
    ax.set(title="Net Sales by City",xlabel="City",ylabel="Net sales (INR)")
    ax.tick_params(axis="x",rotation=20); fig.tight_layout(); fig.savefig(CHART_DIR/"sales_by_city.png",dpi=160); plt.close(fig)
    payments=df["payment_method"].value_counts().rename_axis("payment_method").reset_index(name="orders")
    fig,ax=plt.subplots(figsize=(8,5)); ax.bar(payments["payment_method"], payments["orders"])
    ax.set(title="Orders by Payment Method",xlabel="Payment method",ylabel="Orders")
    fig.tight_layout(); fig.savefig(CHART_DIR/"payment_method_mix.png",dpi=160); plt.close(fig)
    print("EDA complete.")
    print(f"Rows analyzed: {len(df):,}")
    print(f"Net sales: INR {metrics['net_sales_inr']:,.2f}")
    print(f"Top category: {metrics['top_category_by_net_sales']}")
    print(f"Top city: {metrics['top_city_by_net_sales']}")
    print(f"Outputs saved to: {OUTPUT_DIR}")
if __name__ == "__main__":
    main()
