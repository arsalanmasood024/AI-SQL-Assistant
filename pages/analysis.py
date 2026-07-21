import streamlit as st

from Analytics.customer import top_customers
from Analytics.sale import monthly_sales
from Analytics.product import top_products
from Analytics.employee import employee_performance
from Analytics.inventory import low_stock

st.title("📊 Analytics Dashboard")

if st.button("Top Customers"):

    st.dataframe(top_customers())

if st.button("Monthly Sales"):

    st.dataframe(monthly_sales())

if st.button("Top Products"):

    st.dataframe(top_products())

if st.button("Employee Performance"):

    st.dataframe(employee_performance())

if st.button("Low Stock"):

    st.dataframe(low_stock())