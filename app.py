import streamlit as st
from diagnose import diagnose


st.title("🚗 AutoBuddy AI")

st.write(
    "AI Automotive Troubleshooting Assistant"
)


problem = st.text_area(
    "Describe your vehicle problem"
)


if st.button("Diagnose"):

    if problem:

        with st.spinner("Analyzing problem..."):

            result = diagnose(problem)


        st.subheader("Diagnostic Report")

        st.write(result)


    else:

        st.warning(
            "Please enter a vehicle problem"
        )