import streamlit as st

st.title("📜 Query History")

history = st.session_state.get("history", [])

if not history:

    st.info("No history.")

else:

    for i, q in enumerate(reversed(history), 1):

        st.write(f"{i}. {q}")