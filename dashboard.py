
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Retail Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Retail Sales Analysis Dashboard")
st.write("Analyze revenue, products, and sales trends.")

df = pd.read_csv("sales.csv")
df["Revenue"] = df["Quantity"] * df["Unit_Price"]
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# Filters
st.sidebar.header("Filters")

categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

products = st.sidebar.multiselect(
    "Select Product",
    options=sorted(df["Product"].unique()),
    default=sorted(df["Product"].unique())
)

filtered_df = df[
    df["Category"].isin(categories) &
    df["Product"].isin(products)
]

if filtered_df.empty:
    st.warning("No sales records match your filters.")
    st.stop()

# Summary metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹{filtered_df['Revenue'].sum():,.0f}")
col2.metric("Units Sold", int(filtered_df["Quantity"].sum()))
col3.metric("Sales Records", len(filtered_df))

# Revenue by product
st.subheader("Revenue by Product")
product_sales = filtered_df.groupby("Product")["Revenue"].sum()
st.bar_chart(product_sales, y_label="Revenue (₹)")

# Revenue by category
st.subheader("Revenue by Category")
category_sales = filtered_df.groupby("Category")["Revenue"].sum()
st.bar_chart(category_sales, y_label="Revenue (₹)")

# Monthly revenue
st.subheader("Monthly Revenue")
monthly_sales = filtered_df.groupby("Month")["Revenue"].sum()
st.line_chart(monthly_sales, y_label="Revenue (₹)")

# Business Insights
st.subheader("💡 Business Insights")

top_product = product_sales.idxmax()
top_category = category_sales.idxmax()
best_month = monthly_sales.idxmax()

col1, col2, col3 = st.columns(3)

col1.info(f"Top Revenue Product: {top_product}")
col2.info(f"Top Revenue Category: {top_category}")
col3.info(f"Best Sales Month: {best_month}")

# Data table
st.subheader("Sales Records")
st.dataframe(filtered_df, use_container_width=True)