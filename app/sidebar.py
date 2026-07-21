import streamlit as st


EXAMPLES = [
    "Show top 10 customers by sales",
    "Show monthly sales",
    "Show top selling products",
    "Show low stock products",
    "Show employee performance",
    "Show category revenue",
]


def init_sidebar():

    st.sidebar.title("🤖 AI SQL Assistant")

    st.sidebar.markdown("---")

    st.sidebar.subheader("📊 Example Questions")

    for question in EXAMPLES:

        if st.sidebar.button(question, use_container_width=True):

            st.session_state["selected_question"] = question

    st.sidebar.markdown("---")

    st.sidebar.subheader("🕒 Query History")

    history = st.session_state.get("history", [])

    if history:

        for i, q in enumerate(reversed(history[-10:])):

            if st.sidebar.button(q,
            key=f"history_{i}",
            use_container_width=True
        ): st.session_state["selected_question"] = q

    else:

        st.sidebar.caption("No queries yet.")
        st.sidebar.markdown("---")

        st.sidebar.subheader("📊 Statistics")

        st.sidebar.metric(
            "Queries Run",
            st.session_state.get("query_count", 0)
        )

        st.sidebar.metric(
            "Rows Returned",
            st.session_state.get("rows_returned", 0)
        )
    st.sidebar.markdown("---")

    st.sidebar.subheader("🗄 Database")

    st.sidebar.markdown("""
        **Tables**

        - Customers
        - Products
        - Categories
        - Suppliers
        - Employees
        - Orders
        - OrderItems
        - Inventory
        """)

    st.sidebar.markdown("---")

    if st.sidebar.button("🧹 Clear Chat", use_container_width=True):

        st.session_state.messages = []
        st.session_state.history = []

        st.rerun()

    st.sidebar.markdown("---")

    st.sidebar.caption("Version 1.0 By ARSALAN MASOOD")
    st.sidebar.caption("Built with Streamlit + Ollama + SQL Server")

    return st.sidebar