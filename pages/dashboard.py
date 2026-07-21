import streamlit as st

st.title("🏠 Dashboard")

st.metric(
    "Queries",
    st.session_state.get("query_count", 0)
)

st.metric(
    "Rows Returned",
    st.session_state.get("rows_returned", 0)
)

st.metric(
    "History",
    len(st.session_state.get("history", []))
)