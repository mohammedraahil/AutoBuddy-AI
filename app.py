import streamlit as st
from diagnose import diagnose


st.title("🚗 AutoBuddy AI")

st.write(
    "Intelligent Automotive Troubleshooting Assistant"
)


# Vehicle details

st.subheader("Vehicle Information")


make = st.text_input(
    "Vehicle Make",
    placeholder="Example: Honda"
)


model = st.text_input(
    "Vehicle Model",
    placeholder="Example: Brio"
)


year = st.text_input(
    "Manufacturing Year",
    placeholder="Example: 2018"
)


mileage = st.number_input(
    "Mileage (km)",
    min_value=0,
    step=5000
)



problem = st.text_area(
    "Describe the problem",
    placeholder="Example: AC cools at night but weak during afternoon traffic"
)

st.caption(
    "Example: AC weak in traffic, engine overheating, strange noise while braking"
)


if st.button("Diagnose"):


    if problem:


        vehicle_info = f"""
        Vehicle:
        {make} {model}
        Year:
        {year}
        Mileage:
        {mileage}

        Problem:
        {problem}
        """


        with st.spinner(
            "Analyzing vehicle problem..."
        ):


            result = diagnose(
                vehicle_info
            )

        st.subheader("🔍 Diagnostic Report")


        st.markdown(result)

    else:

        st.warning(
            "Please describe the problem"
        )