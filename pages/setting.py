import streamlit as st

st.title("⚙ Settings")

dark = st.toggle(
    "light Theme",
    True
)

chart = st.selectbox(

    "Default Chart",

    [

        "Auto",

        "Bar",

        "Line",

        "Pie"

    ]

)

st.success("Settings saved.")