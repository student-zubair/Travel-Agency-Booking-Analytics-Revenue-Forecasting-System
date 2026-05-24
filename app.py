import streamlit as st
from login import login_page
from dashboard import dashboard_page
from prediction import prediction_page

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Travel Revenue Forecasting",
    layout="wide"
)

# ==================================================
# SESSION STATE
# ==================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ==================================================
# LOGIN
# ==================================================

if not st.session_state.logged_in:

    login_page()

# ==================================================
# MAIN APP
# ==================================================

else:

    st.sidebar.title("Navigation")

    page = st.sidebar.radio(
        "Go To",
        [
            "Dashboard",
            "Prediction"
        ]
    )

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False

        st.rerun()

    if page == "Dashboard":

        dashboard_page()

    elif page == "Prediction":

        prediction_page()