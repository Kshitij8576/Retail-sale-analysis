import streamlit as st
import pandas as pd

# Page title
st.title("Retail Sales Analysis")

# Load data
df = pd.read_csv("sales.csv")

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Calculate sales
df["Sales"] = df["Quantity"] * df["Unit_Price"]

# Basic calculations
total_sales = df["Sales"].sum()
total_orders = df["Order_ID"].nunique()
total_quantity = df["Quantity"].sum()
average_order = df.groupby("Order_ID")["Sales"].sum().mean()

# Display KPIs
st.subheader("Sales Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"₹{total_sales:,.0f}")
col2.metric("Total Orders", total_orders)
col3.metric("Total Quantity", total_quantity)
col4.metric("Average Order", f"₹{average_order:,.0f}")

# Sales by category
st.subheader("Sales by Category")

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_sales)

# Monthly sales
st.subheader("Monthly Sales")

monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

st.line_chart(monthly_sales)

# Sales by city
st.subheader("Sales by City")

city_sales = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(city_sales)

# Top products
st.subheader("Top 10 Products")

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(product_sales)

# Show data
st.subheader("Sales Data")

st.dataframe(df, use_container_width=True)
