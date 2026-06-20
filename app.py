import streamlit as st

from rag import db


st.title("AutoDiagnose AI 🚗")


problem = st.text_input(
"Describe vehicle problem"
)



if st.button("Diagnose"):


    results=db.similarity_search(
        problem,
        k=3
    )


    st.subheader(
    "Relevant Knowledge"
    )


    for r in results:

        st.write(
        r.page_content
        )