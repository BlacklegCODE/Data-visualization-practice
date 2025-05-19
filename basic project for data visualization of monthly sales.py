import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sales = pd.read_csv("sales_data.csv")

sales["Order Date"] = pd.to_datetime(sales["Order Date"])
sales["Month"] = sales["Order Date"].dt.to_period("M")

monthly_sales = sales.groupby("Month")["Sales"].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x="Month", y="Sales", data=monthly_sales, marker="o")
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.tight_layout()
plt.show()

category_sales = sales.groupby("Category")["Sales"].sum().reset_index().sort_values(by="Sales", ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x="Sales", y="Category", data=category_sales, palette="viridis")
plt.title("Sales by Category")
plt.tight_layout()
plt.show()

region_profit = sales.groupby("Region")["Profit"].sum().reset_index().sort_values(by="Profit")

plt.figure(figsize=(8, 5))
sns.barplot(x="Profit", y="Region", data=region_profit, palette="coolwarm")
plt.title("Profit by Region")
plt.tight_layout()
plt.show()
