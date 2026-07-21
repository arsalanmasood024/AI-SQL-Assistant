import streamlit as st

from AI.sql_generator import generate_sql
from AI.validator import validate_sql
from AI.executor import execute_sql
from AI.explainer import explain_sql
from styles import load_css
from charts import auto_chart
from export import to_csv, to_excel
from sidebar import init_sidebar
from chat import *
from utils import show_metrics

if "history" not in st.session_state:
    st.session_state.history = []

if "messages" not in st.session_state:
    st.session_state.messages = []

if "sql_history" not in st.session_state:
    st.session_state.sql_history = []
    
st.set_page_config(
    page_title="AI SQL Assistant",
    page_icon="🤖",
    layout="wide"
)



st.markdown(load_css(), unsafe_allow_html=True)



init_sidebar()
init_chat()
show_chat()



st.title("🤖 AI SQL Assistant")

st.write(
    "Ask questions about your SQL Server database using natural language."
)



if "query_count" not in st.session_state:
    st.session_state.query_count = 0

if "rows_returned" not in st.session_state:
    st.session_state.rows_returned = 0



question = st.chat_input(
    "Ask anything about your database..."
)



if question:

    add_user_message(question)

    with st.chat_message("user"):
        st.markdown(question)

        status = st.status(
        "🤖 AI is thinking...",
        expanded=True
)

        status.write("🧠 Understanding your question...")
        status.write("📝 Generating SQL...")

        status.write("🛡 Validating SQL...")

        status.write("🗄 Executing query...")

        status.write("📊 Creating chart...")

        status.write("📈 Preparing results...")

        sql = generate_sql(question)
        status.write("🗄 Executing SQL...")

    valid, sql = validate_sql(sql)
    explanation = explain_sql(sql)

    if not valid:
        st.error(sql)
        st.stop()

    df, elapsed, error = execute_sql(sql)
    status.write("📊 Creating visualization...")
    status.update(
        label="✅ Completed",
        state="complete"
    )

    if error:
        st.error(error)
        st.stop()

    # Save history

    if question not in st.session_state.history:
        st.session_state.history.append(question)

    add_ai_message("Query executed successfully.")

    with st.chat_message("assistant"):

        st.success("✅ SQL generated and executed successfully.")

      

        with st.expander("Generated SQL"):

            st.code(sql, language="sql")
            st.subheader("🧠 Explanation")

            st.info(explanation)

        

        show_metrics(df, elapsed)

        

        st.subheader("Results")

        st.dataframe(
            df,
            use_container_width=True
        )

    

        fig = auto_chart(df)

        if fig:

            st.plotly_chart(
                fig,
                use_container_width=True
            )

       

        st.divider()

        st.subheader("📥 Export Results")

        col1, col2 = st.columns(2)

        with col1:

            st.download_button(
                "📄 Download CSV",
                data=to_csv(df),
                file_name="results.csv",
                use_container_width=True
            )

        with col2:

            st.download_button(
                "📗 Download Excel",
                data=to_excel(df),
                file_name="results.xlsx",
                use_container_width=True
            )