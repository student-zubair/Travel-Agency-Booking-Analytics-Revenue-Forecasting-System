import streamlit as st
import pandas as pd
import plotly.express as px
import os

# =========================================================
# PATH SETUP
# =========================================================

BASE_DIR = os.path.dirname(__file__)

DATA_DIR = os.path.join(BASE_DIR, "Data")

# =========================================================
# LOAD DATASETS
# =========================================================

bookings_df = pd.read_csv(
    os.path.join(DATA_DIR, "bookings.csv")
)

passengers_df = pd.read_csv(
    os.path.join(DATA_DIR, "passengers.csv")
)

payments_df = pd.read_csv(
    os.path.join(DATA_DIR, "payments.csv")
)

segments_df = pd.read_csv(
    os.path.join(DATA_DIR, "segments.csv")
)

# =========================================================
# DATE CONVERSION
# =========================================================

bookings_df["booking_date"] = pd.to_datetime(
    bookings_df["booking_date"]
)

bookings_df["travel_date"] = pd.to_datetime(
    bookings_df["travel_date"]
)

payments_df["payment_date"] = pd.to_datetime(
    payments_df["payment_date"]
)

# =========================================================
# DASHBOARD FUNCTION
# =========================================================

def dashboard_page():

    st.title("✈️ Travel Revenue Analytics Dashboard")

    # =====================================================
    # KPI SECTION
    # =====================================================

    total_revenue = bookings_df["total_usd"].sum()

    total_profit = bookings_df["profit_usd"].sum()

    total_bookings = bookings_df.shape[0]

    total_passengers = passengers_df.shape[0]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Revenue",
        f"${total_revenue:,.0f}"
    )

    col2.metric(
        "Total Profit",
        f"${total_profit:,.0f}"
    )

    col3.metric(
        "Total Bookings",
        f"{total_bookings:,}"
    )

    col4.metric(
        "Total Passengers",
        f"{total_passengers:,}"
    )

    st.divider()

    # =====================================================
    # SIDEBAR FILTERS
    # =====================================================

    st.sidebar.header("Filters")

    selected_cabin = st.sidebar.multiselect(
        "Cabin",
        bookings_df["cabin"].unique(),
        default=bookings_df["cabin"].unique()
    )

    selected_trip = st.sidebar.multiselect(
        "Trip Type",
        bookings_df["trip_type"].unique(),
        default=bookings_df["trip_type"].unique()
    )

    selected_status = st.sidebar.multiselect(
        "Booking Status",
        bookings_df["booking_status"].unique(),
        default=bookings_df["booking_status"].unique()
    )

    filtered_df = bookings_df[
        (bookings_df["cabin"].isin(selected_cabin)) &
        (bookings_df["trip_type"].isin(selected_trip)) &
        (bookings_df["booking_status"].isin(selected_status))
    ]

    # =====================================================
    # REVENUE BY CABIN
    # =====================================================

    st.subheader("💺 Revenue by Cabin")

    cabin_rev = (
        filtered_df.groupby("cabin")["total_usd"]
        .sum()
        .reset_index()
    )

    fig1 = px.bar(
        cabin_rev,
        x="cabin",
        y="total_usd",
        color="cabin",
        text_auto=True
    )

    st.plotly_chart(
        fig1,
        use_container_width=True,
        key="revenue_by_cabin"
    )

    # =====================================================
    # BOOKING STATUS
    # =====================================================

    st.subheader("📌 Booking Status Distribution")

    booking_status = (
        filtered_df["booking_status"]
        .value_counts()
        .reset_index()
    )

    booking_status.columns = ["Status", "Count"]

    fig2 = px.pie(
        booking_status,
        names="Status",
        values="Count",
        hole=0.4
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
        key="booking_status"
    )

    # =====================================================
    # MONTHLY REVENUE TREND
    # =====================================================

    st.subheader("📈 Monthly Revenue Trend")

    filtered_df["month"] = (
        filtered_df["booking_date"]
        .dt.to_period("M")
        .astype(str)
    )

    monthly_rev = (
        filtered_df.groupby("month")["total_usd"]
        .sum()
        .reset_index()
    )

    fig3 = px.line(
        monthly_rev,
        x="month",
        y="total_usd",
        markers=True
    )

    st.plotly_chart(
        fig3,
        use_container_width=True,
        key="monthly_revenue"
    )

    # =====================================================
    # TOP AIRLINES
    # =====================================================

    st.subheader("✈️ Top Airlines by Revenue")

    airline_rev = (
        filtered_df.groupby("airline")["total_usd"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig4 = px.bar(
        airline_rev,
        x="airline",
        y="total_usd",
        color="airline",
        text_auto=True
    )

    st.plotly_chart(
        fig4,
        use_container_width=True,
        key="top_airlines"
    )

    # =====================================================
    # TOP DESTINATIONS
    # =====================================================

    st.subheader("🌍 Top Destinations")

    destination_data = (
        filtered_df.groupby("destination")["total_usd"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig5 = px.bar(
        destination_data,
        x="destination",
        y="total_usd",
        color="destination",
        text_auto=True
    )

    st.plotly_chart(
        fig5,
        use_container_width=True,
        key="top_destinations"
    )

    # =====================================================
    # PAYMENT METHODS
    # =====================================================

    st.subheader("💳 Payment Method Usage")

    payment_data = (
        payments_df["payment_method"]
        .value_counts()
        .reset_index()
    )

    payment_data.columns = [
        "Payment Method",
        "Count"
    ]

    fig6 = px.pie(
        payment_data,
        names="Payment Method",
        values="Count"
    )

    st.plotly_chart(
        fig6,
        use_container_width=True,
        key="payment_methods"
    )

    # =====================================================
    # PASSENGER GENDER DISTRIBUTION
    # =====================================================

    st.subheader("🧑 Passenger Gender Distribution")

    gender_data = (
        passengers_df["gender"]
        .value_counts()
        .reset_index()
    )

    gender_data.columns = [
        "Gender",
        "Count"
    ]

    fig7 = px.bar(
        gender_data,
        x="Gender",
        y="Count",
        color="Gender",
        text_auto=True
    )

    st.plotly_chart(
        fig7,
        use_container_width=True,
        key="gender_distribution"
    )

    # =====================================================
    # PASSENGER NATIONALITY
    # =====================================================

    st.subheader("🌎 Top Passenger Nationalities")

    nationality_data = (
        passengers_df["nationality"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    nationality_data.columns = [
        "Nationality",
        "Count"
    ]

    fig8 = px.bar(
        nationality_data,
        x="Nationality",
        y="Count",
        color="Nationality",
        text_auto=True
    )

    st.plotly_chart(
        fig8,
        use_container_width=True,
        key="top_nationalities"
    )

    # =====================================================
    # STOP TYPE DISTRIBUTION
    # =====================================================

    st.subheader("🛫 Stop Type Distribution")

    stop_data = (
        segments_df["stop_type"]
        .value_counts()
        .reset_index()
    )

    stop_data.columns = [
        "Stop Type",
        "Count"
    ]

    fig9 = px.pie(
        stop_data,
        names="Stop Type",
        values="Count"
    )

    st.plotly_chart(
        fig9,
        use_container_width=True,
        key="stop_distribution"
    )

    # =====================================================
    # TOP ROUTES
    # =====================================================

    st.subheader("🗺️ Top Routes")

    route_data = (
        filtered_df.groupby(
            ["origin", "destination"]
        )["total_usd"]
        .sum()
        .reset_index()
    )

    route_data["Route"] = (
        route_data["origin"]
        + " → " +
        route_data["destination"]
    )

    route_data = (
        route_data.sort_values(
            by="total_usd",
            ascending=False
        )
        .head(10)
    )

    fig10 = px.bar(
        route_data,
        x="Route",
        y="total_usd",
        color="Route",
        text_auto=True
    )

    st.plotly_chart(
        fig10,
        use_container_width=True,
        key="top_routes"
    )

    # =====================================================
    # DATA PREVIEW
    # =====================================================

    st.subheader("📄 Bookings Dataset Preview")

    st.dataframe(
        filtered_df.head(20),
        use_container_width=True
    )