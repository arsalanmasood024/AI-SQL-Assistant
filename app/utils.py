import streamlit as st


def show_sql(sql):

    st.subheader("Generated SQL")

    st.code(sql, language="sql")


def show_metrics(df, elapsed):

    c1, c2 = st.columns(2)

    c1.metric("Rows", len(df))

    c2.metric("Execution Time", f"{elapsed:.3f}s")