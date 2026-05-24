import streamlit as st
import pandas as pd
import joblib

# =========================================================
# LOAD FILES
# =========================================================

model = joblib.load("xgb_travel_model.pkl")
encoders = joblib.load("label_encoders.pkl")
feature_columns = joblib.load("feature_names.pkl")

# =========================================================
# ALL CATEGORICAL VALUES
# =========================================================

ROUTE_BAND = [
    'Medium', 'Long', 'Short', 'VeryLong'
]

CABIN = [
    'PremiumEconomy', 'Economy', 'Business', 'First'
]

REGION = [
    'Subcontinent', 'MiddleEast', 'Americas', 'GCC',
    'Europe', 'Australia', 'Africa',
    'SoutheastAsia', 'EastAsia'
]

ORIGIN_REGION = [
    'GCC', 'Africa', 'MiddleEast', 'Europe',
    'Subcontinent', 'EastAsia', 'Australia',
    'Americas', 'SoutheastAsia'
]

STOP_TYPE = [
    'Direct', 'Connection'
]

AIRLINE = [
    'WY', 'ME', 'UK', 'KU', 'ET', '6E', 'EK', 'SV', 'G9', 'JQ',
    'KQ', 'TK', 'AK', 'FZ', 'LX', 'OS', 'PK', 'BG', 'UA', 'QR',
    'EY', 'BR', 'NH', 'RJ', 'KE', 'W6', 'GF', 'AZ', 'AI', 'XY',
    'IB', 'IA', 'SA', 'AF', 'CA', 'MS', 'GA', 'LH', 'PC', 'UL',
    'SG', 'VN', 'DL', 'AA', 'BA', 'VA', 'PR', 'AC', 'SQ', 'TG',
    'FR', 'MU', 'MH', 'QF', 'CX', 'KL'
]

BOOKING_DAY = [
    'Monday', 'Wednesday', 'Saturday',
    'Sunday', 'Thursday', 'Tuesday', 'Friday'
]

DESTINATION = [
    'DAC', 'BEY', 'CMB', 'CAI', 'YYZ', 'MAA', 'BAH', 'DMM',
    'MXP', 'AMM', 'MEL', 'SAW', 'DEL', 'LOS', 'HAN', 'SGN',
    'VIE', 'MAN', 'ATH', 'TBS', 'KHI', 'ORD', 'IAD', 'DOH',
    'KRT', 'TLV', 'AUH', 'MED', 'SKT', 'HYD', 'PEK', 'MUX',
    'DAR', 'ZRH', 'LAX', 'MCT', 'EVN', 'TPE', 'BSR', 'FCO',
    'BGW', 'KUL', 'SIN', 'AMS', 'RUH', 'BOM', 'PER', 'HKG',
    'ALG', 'LHR', 'SYD', 'NRT', 'NBO', 'JED', 'IST', 'BKK',
    'PEW', 'MAD', 'LHE', 'BLR', 'MNL', 'CDG', 'DXB', 'SHJ',
    'GRU', 'CGK', 'PVG', 'NJF', 'JNB', 'ADL', 'SSH', 'ISB',
    'FRA', 'ICN', 'CCU', 'ADD', 'CMN', 'BNE', 'KWI', 'HRG',
    'BCN', 'JFK'
]

ORIGIN_CITY = [
    'Sharjah', 'Kuwait City', 'Casablanca', 'Dubai', 'Manama',
    'Algiers', 'Abu Dhabi', 'Riyadh', 'Najaf', 'Jeddah',
    'Athens', 'Nairobi', 'Hyderabad', 'Seoul', 'Dammam',
    'Dar es Salaam', 'Tokyo', 'Beijing', 'Melbourne',
    'Chicago', 'Frankfurt', 'Baghdad', 'Bengaluru',
    'Islamabad', 'Muscat', 'Madrid', 'Yerevan', 'Paris',
    'Tbilisi', 'Johannesburg', 'Istanbul-SAW', 'Rome',
    'Zurich', 'Doha', 'Medina', 'Milan', 'Karachi',
    'Washington DC', 'Manila', 'Sao Paulo', 'New York',
    'Sydney', 'Lahore', 'Brisbane', 'Dhaka', 'Colombo',
    'Sharm El Sheikh', 'Amman', 'Peshawar', 'Tel Aviv',
    'Kuala Lumpur', 'New Delhi', 'Istanbul', 'London',
    'Manchester', 'Adelaide', 'Khartoum', 'Jakarta',
    'Multan', 'Chennai', 'Beirut', 'Vienna', 'Toronto',
    'Lagos', 'Perth', 'Basra', 'Amsterdam', 'Sialkot',
    'Shanghai', 'Bangkok', 'Taipei', 'Hanoi', 'Hurghada',
    'Singapore', 'Cairo', 'Los Angeles', 'Barcelona',
    'Mumbai', 'Hong Kong', 'Addis Ababa', 'Kolkata',
    'Ho Chi Minh'
]

CITY = [
    'Dhaka', 'Beirut', 'Colombo', 'Cairo', 'Toronto',
    'Chennai', 'Manama', 'Dammam', 'Milan', 'Amman',
    'Melbourne', 'Istanbul-SAW', 'New Delhi', 'Lagos',
    'Hanoi', 'Ho Chi Minh', 'Vienna', 'Manchester',
    'Athens', 'Tbilisi', 'Karachi', 'Chicago',
    'Washington DC', 'Doha', 'Khartoum', 'Tel Aviv',
    'Abu Dhabi', 'Medina', 'Sialkot', 'Hyderabad',
    'Beijing', 'Multan', 'Dar es Salaam', 'Zurich',
    'Los Angeles', 'Muscat', 'Yerevan', 'Taipei',
    'Basra', 'Rome', 'Baghdad', 'Kuala Lumpur',
    'Singapore', 'Amsterdam', 'Riyadh', 'Mumbai',
    'Perth', 'Hong Kong', 'Algiers', 'London',
    'Sydney', 'Tokyo', 'Nairobi', 'Jeddah', 'Istanbul',
    'Bangkok', 'Peshawar', 'Madrid', 'Lahore',
    'Bengaluru', 'Manila', 'Paris', 'Dubai',
    'Sharjah', 'Sao Paulo', 'Jakarta', 'Shanghai',
    'Najaf', 'Johannesburg', 'Adelaide',
    'Sharm El Sheikh', 'Islamabad', 'Frankfurt',
    'Seoul', 'Kolkata', 'Addis Ababa', 'Casablanca',
    'Brisbane', 'Kuwait City', 'Hurghada',
    'Barcelona', 'New York'
]

HOME_REGION = [
    'GCC', 'MiddleEast', 'Subcontinent',
    'Africa', 'Australia', 'Europe',
    'SoutheastAsia', 'Americas', 'EastAsia'
]

TRIP_TYPE = [
    'One-way', 'Round-trip', 'Multi-city'
]

PAYMENT_METHOD = [
    'KNet', 'Cash', 'Payment Link',
    'Card', 'Online Transfer', 'Bank Transfer'
]

ORIGIN = [
    'SHJ', 'KWI', 'CMN', 'DXB', 'BAH', 'ALG', 'AUH',
    'RUH', 'NJF', 'JED', 'ATH', 'NBO', 'HYD', 'ICN',
    'DMM', 'DAR', 'NRT', 'PEK', 'MEL', 'ORD', 'FRA',
    'BGW', 'BLR', 'ISB', 'MCT', 'MAD', 'EVN', 'CDG',
    'TBS', 'JNB', 'SAW', 'FCO', 'ZRH', 'DOH', 'MED',
    'MXP', 'KHI', 'IAD', 'MNL', 'GRU', 'JFK', 'SYD',
    'LHE', 'BNE', 'DAC', 'CMB', 'SSH', 'AMM', 'PEW',
    'TLV', 'KUL', 'DEL', 'IST', 'LHR', 'MAN', 'ADL',
    'KRT', 'CGK', 'MUX', 'MAA', 'BEY', 'VIE', 'YYZ',
    'LOS', 'PER', 'BSR', 'AMS', 'SKT', 'PVG', 'BKK',
    'TPE', 'HAN', 'HRG', 'SIN', 'CAI', 'LAX', 'BCN',
    'BOM', 'HKG', 'ADD', 'CCU', 'SGN'
]

NATIONALITY = [
    'Kuwaiti', 'Qatari', 'Bahraini', 'Lebanese',
    'Canadian', 'Emirati', 'German', 'Australian',
    'Nigerian', 'Pakistani', 'Indonesian', 'Filipino',
    'Sri Lankan', 'Saudi', 'British', 'Kenyan',
    'Indian', 'Egyptian', 'Ethiopian', 'Nepali',
    'Omani', 'Chinese', 'Syrian', 'Spanish',
    'American', 'Thai', 'French', 'Japanese',
    'Iraqi', 'Korean', 'Jordanian', 'Bangladeshi',
    'Turkish', 'South African', 'Italian',
    'New Zealander', 'Malaysian', 'Brazilian'
]

AIRLINE_NAME = [
    'Oman Air', 'Middle East Airlines', 'Vistara',
    'Kuwait Airways', 'Ethiopian Airlines', 'IndiGo',
    'Emirates', 'Saudia', 'Air Arabia Abu Dhabi',
    'Jetstar', 'Kenya Airways', 'Turkish Airlines',
    'AirAsia', 'Flydubai', 'Swiss', 'Austrian',
    'PIA', 'Biman Bangladesh', 'United Airlines',
    'Qatar Airways', 'Etihad Airways', 'EVA Air',
    'ANA', 'Royal Jordanian', 'Korean Air',
    'Wizz Air', 'Gulf Air', 'ITA Airways',
    'Air India', 'flynas', 'Iberia',
    'Iraqi Airways', 'South African Airways',
    'Air France', 'Air China', 'EgyptAir',
    'Garuda Indonesia', 'Lufthansa',
    'Pegasus Airlines', 'SriLankan Airlines',
    'SpiceJet', 'Vietnam Airlines',
    'Delta Air Lines', 'American Airlines',
    'British Airways', 'Virgin Australia',
    'Philippine Airlines', 'Air Canada',
    'Singapore Airlines', 'Thai Airways',
    'Ryanair', 'China Eastern',
    'Malaysia Airlines', 'Qantas',
    'Cathay Pacific', 'KLM'
]

GENDER = ['F', 'M']

# =========================================================
# PAGE
# =========================================================

def prediction_page():

    st.title("🤖 Revenue Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:

        route_band = st.selectbox("Route Band", ROUTE_BAND)
        cabin = st.selectbox("Cabin", CABIN)
        pax_count = st.slider("Passenger Count", 1, 10, 1)
        region = st.selectbox("Region", REGION)
        origin_region = st.selectbox("Origin Region", ORIGIN_REGION)
        total_duration = st.number_input("Total Duration", 30, 3000, 300)
        booking_month = st.slider("Booking Month", 1, 12, 1)
        stop_type = st.selectbox("Stop Type", STOP_TYPE)

    with col2:

        airline = st.selectbox("Airline", AIRLINE)
        total_legs = st.slider("Total Legs", 1, 5, 1)
        booking_dayofweek = st.selectbox("Booking Day", BOOKING_DAY)
        lead_time_days = st.slider("Lead Time Days", 1, 365, 30)
        loyalty_members = st.slider("Loyalty Members", 0, 5, 0)
        destination = st.selectbox("Destination", DESTINATION)
        origin_city = st.selectbox("Origin City", ORIGIN_CITY)
        city = st.selectbox("Destination City", CITY)

    with col3:

        home_region = st.selectbox("Home Region", HOME_REGION)
        booking_year = st.slider("Booking Year", 2020, 2030, 2025)
        trip_type = st.selectbox("Trip Type", TRIP_TYPE)
        payment_method = st.selectbox("Payment Method", PAYMENT_METHOD)
        origin = st.selectbox("Origin Airport", ORIGIN)
        nationality = st.selectbox("Nationality", NATIONALITY)
        airline_name = st.selectbox("Airline Name", AIRLINE_NAME)
        gender = st.selectbox("Gender", GENDER)

    input_data = {
        'route_band': route_band,
        'cabin': cabin,
        'pax_count': pax_count,
        'region': region,
        'origin_region': origin_region,
        'total_duration': total_duration,
        'booking_month': booking_month,
        'stop_type': stop_type,
        'airline': airline,
        'total_legs': total_legs,
        'booking_dayofweek': booking_dayofweek,
        'lead_time_days': lead_time_days,
        'loyalty_members': loyalty_members,
        'destination': destination,
        'origin_city': origin_city,
        'city': city,
        'home_region': home_region,
        'booking_year': booking_year,
        'trip_type': trip_type,
        'payment_method': payment_method,
        'origin': origin,
        'nationality': nationality,
        'airline_name': airline_name,
        'gender': gender
    }

    input_df = pd.DataFrame([input_data])

    # =========================================================
    # CATEGORICAL COLUMNS
    # =========================================================

    categorical_columns = [
        'route_band',
        'cabin',
        'region',
        'origin_region',
        'stop_type',
        'airline',
        'booking_dayofweek',
        'destination',
        'origin_city',
        'city',
        'home_region',
        'trip_type',
        'payment_method',
        'origin',
        'nationality',
        'airline_name',
        'gender'
    ]

    # =========================================================
    # LABEL ENCODING
    # =========================================================

    for col in categorical_columns:

        try:

            input_df[col] = encoders[col].transform(
                input_df[col].astype(str)
            )

        except Exception as e:

            input_df[col] = 0

    # =========================================================
    # MATCH MODEL COLUMNS
    # =========================================================

    for col in feature_columns:

        if col not in input_df.columns:

            input_df[col] = 0

    # =========================================================
    # REORDER COLUMNS
    # =========================================================

    input_df = input_df[feature_columns]

    # =========================================================
    # CONVERT TO NUMERIC
    # =========================================================

    input_df = input_df.apply(pd.to_numeric, errors='coerce')

    # =========================================================
    # HANDLE NULLS
    # =========================================================

    input_df = input_df.fillna(0)
    # =========================================================
    # PREDICT
    # =========================================================

    if st.button("Predict Revenue"):

        prediction = model.predict(input_df)

        st.success(
            f"Predicted Revenue: ${prediction[0]:,.2f}"
        )