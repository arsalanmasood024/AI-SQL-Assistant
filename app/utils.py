import streamlit as st


def show_metrics(df, elapsed):

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📄 Rows Returned",
            len(df)
        )

    with col2:
        st.metric(
            "📋 Columns",
            len(df.columns)
        )

    with col3:
        st.metric(
            "⚡ Execution Time",
            f"{elapsed:.3f} sec"
        )