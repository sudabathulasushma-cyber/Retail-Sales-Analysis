
import pandas as pd

# Load the sales dataset
df = pd.read_csv("sales.csv")

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

# Category analysis
category_sales = df.groupby("Category")["Revenue"].sum()

print("Revenue by Category:")
print(category_sales)

print("\nTop Revenue Category:")
print(category_sales.idxmax())

# Key business metrics
total_units = df["Quantity"].sum()
average_revenue = df["Revenue"].mean()
total_records = len(df)

print("\nKey Business Metrics:")
print("Total Units Sold:", total_units)
print("Average Revenue per Sale Record: ₹", round(average_revenue, 2))
print("Number of Sales Records:", total_records)

# Best-selling product by quantity
product_quantity = df.groupby("Product")["Quantity"].sum()

print("\nUnits Sold by Product:")
print(product_quantity)

print("\nBest-Selling Product:")
print(product_quantity.idxmax())
print("Units Sold:", product_quantity.max())

# Monthly revenue chart
import matplotlib.pyplot as plt

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%B")

month_order = ["January", "February", "March", "April",
               "May", "June", "July", "August",
               "September", "October", "November", "December"]

monthly_sales = df.groupby("Month")["Revenue"].sum()
monthly_sales = monthly_sales.reindex(
    [month for month in month_order if month in monthly_sales.index]
)

plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="bar")
plt.title("Monthly Sales Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Sales Summary Report
print("\n========== SALES SUMMARY REPORT ==========")

print("Total Revenue: ₹", round(df["Revenue"].sum(), 2))
print("Total Units Sold:", df["Quantity"].sum())
print("Total Products:", df["Product"].nunique())
print("Total Categories:", df["Category"].nunique())

top_product = df.groupby("Product")["Revenue"].sum().idxmax()
print("Highest Revenue Product:", top_product)

top_month = monthly_sales.idxmax()
print("Best Sales Month:", top_month)

top_category = df.groupby("Category")["Revenue"].sum().idxmax()
print("Highest Revenue Category:", top_category)

print("==========================================")