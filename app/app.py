import streamlit as st

from AI.sql_generator import generate_sql
from AI.validator import validate_sql
from AI.executor import execute_sql

from styles import load_css
from utils import show_sql, show_metrics
from charts import auto_chart
from export import to_csv, to_excel


st.set_page_config(
    page_title="AI SQL Assistant",
    page_icon="🤖",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

st.title("🤖 AI SQL Assistant")

st.write(
    "Ask questions about your SQL Server database using natural language."
)

question = st.text_input(
    "Question",
    placeholder="Show top 10 customers by sales"
)

if st.button("Ask AI"):

    if question == "":
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Generating SQL..."):

        sql = generate_sql(question)

    valid, sql = validate_sql(sql)

    if not valid:
        st.error(sql)
        st.stop()

    df, elapsed, error = execute_sql(sql)

    if error:
        st.error(error)
        st.stop()

    show_sql(sql)

    show_metrics(df, elapsed)

    st.subheader("Results")

    st.dataframe(df, use_container_width=True)

    fig = auto_chart(df)

    if fig:

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.download_button(
        "Download CSV",
        data=to_csv(df),
        file_name="results.csv"
    )

    st.download_button(
        "Download Excel",
        data=to_excel(df),
        file_name="results.xlsx"
    )