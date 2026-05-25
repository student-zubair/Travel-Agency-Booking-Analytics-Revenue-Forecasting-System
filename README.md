# ✈️ Travel Agency Booking Analytics & Revenue Forecasting System

An end-to-end analytics and predictive intelligence project developed using **Snowflake, Python, Power BI, Machine Learning, Databricks, and Streamlit** to analyze airline booking operations, passenger behavior, seasonal revenue trends, and revenue forecasting.

---

# 📌 Project Overview

This project transforms raw airline operational data into a centralized analytics and forecasting platform capable of:

* Monitoring booking and revenue performance
* Analyzing customer and travel behavior
* Identifying profitable routes and cabin classes
* Forecasting future booking revenue using Machine Learning
* Delivering interactive dashboards and web-based analytics

---

# 🎯 Business Problem

Travel agencies generate large volumes of booking, passenger, payment, and airline operational data. However, businesses face several challenges:

* Fragmented operational datasets
* Limited visibility into booking trends and profitability
* Difficulty identifying high-performing routes and cabin segments
* Lack of predictive forecasting capability
* Limited operational intelligence for strategic planning

This project addresses these challenges through centralized analytics, business intelligence, and predictive modeling.

---

# 🚀 Project Objectives

## Business Objectives

* Analyze booking and revenue trends
* Monitor airline and route profitability
* Understand passenger booking behavior
* Identify seasonal demand patterns
* Forecast future booking revenue
* Enable data-driven business decisions

## Technical Objectives

* Perform SQL-based data cleaning and validation
* Conduct exploratory and diagnostic analytics
* Develop Power BI dashboards
* Build machine learning forecasting models
* Deploy an interactive Streamlit application

---

# 🛠️ Technology Stack

| Technology           | Purpose                           |
| -------------------- | --------------------------------- |
| Snowflake            | Data Validation & SQL Analysis    |
| Python               | EDA, Analytics & Machine Learning |
| Databricks           | ML Development Environment        |
| Power BI             | Interactive Dashboards            |
| Streamlit            | Web Application Deployment        |
| Scikit-Learn         | ML Modeling                       |
| XGBoost              | Advanced Forecasting Model        |
| Pandas & NumPy       | Data Processing                   |
| Matplotlib & Seaborn | Visualization                     |
| GitHub               | Version Control                   |

---

# 📂 Datasets Used

The project uses multiple relational datasets:

* `bookings.csv`
* `passengers.csv`
* `payments.csv`
* `segments.csv`
* `airports_lookup.csv`
* `airlines_lookup.csv`

---

# 🧹 Data Validation & Cleaning

Performed extensive validation checks including:

* Row count validation
* Duplicate record checks
* Foreign key validation
* Null value checks
* Revenue & profit validation
* Passenger count validation
* Airline and airport lookup validation
* Date consistency validation

---

# ⚙️ Feature Engineering

Additional analytical features were created including:

* Booking Month
* Booking Year
* Route
* Revenue Band
* Profit Margin %
* Booking Type
* Demand Season Type
* Loyalty Category
* Haul Type
* Route Category

---

# 📊 Exploratory Data Analysis (EDA)

EDA was performed to understand operational and revenue behavior using:

* Revenue Distribution Histogram
* Booking Status Analysis
* Revenue by Cabin Class
* Seasonal Revenue Analysis
* Monthly Revenue Trends
* Lead Time vs Revenue Analysis
* Correlation Heatmap

### Key Insights

* Premium cabin classes generated highest revenue
* Summer season contributed maximum booking revenue
* Revenue distribution was highly right-skewed
* Fare and tax variables strongly influenced revenue
* Short lead-time bookings generated higher revenue

---

# 📈 Power BI Dashboards

Interactive dashboards were developed for:

## Business & Sales Overview

* Total Revenue
* Profit Analysis
* Booking Trends
* Airline Performance

## Customer & Booking Analytics

* Passenger Behavior
* Booking Status
* Cabin Analysis
* Seasonal Demand

## Revenue Intelligence

* Revenue Distribution
* Route Profitability
* Operational KPIs

---

# 🤖 Machine Learning Workflow

## Objective

Predict future booking revenue using historical airline operational data.

---

## Models Implemented

### 1. Linear Regression

Baseline regression model

### 2. Random Forest Regressor

Ensemble-based regression model

### 3. XGBoost Regressor

Advanced boosting-based forecasting model

---

# 📉 Model Performance

## Random Forest

| Metric   | Test Score |
| -------- | ---------- |
| MAE      | 897.80     |
| RMSE     | 1672.00    |
| R² Score | 0.8359     |

---

## XGBoost

| Metric   | Test Score |
| -------- | ---------- |
| MAE      | 933.00     |
| RMSE     | 1638.49    |
| R² Score | 0.8424     |

---

# ✅ Final Model Selection

### Selected Model: XGBoost Regressor

### Reason:

* Highest R² Score
* Better generalization capability
* Lower RMSE
* Better forecasting performance on unseen data

---

# 🌐 Streamlit Web Application

The Streamlit application provides:

* Interactive dashboards
* Revenue prediction interface
* Real-time business analytics
* User-friendly forecasting workflow

---

# 📌 Business Recommendations

* Increase focus on premium cabin segments
* Optimize pricing during peak seasons
* Improve cancellation management
* Expand predictive analytics for operational planning
* Develop customer segmentation and loyalty strategies

---

# ⚠️ Challenges Faced

* Handling large relational datasets
* Data cleaning and validation complexity
* Managing skewed revenue distributions
* Preventing ML overfitting
* Integrating dashboards, ML, and deployment workflows

---

# 📚 Key Learnings

* End-to-end analytics workflow implementation
* Advanced EDA and business intelligence
* Revenue forecasting using ML models
* Dashboard development using Power BI
* Streamlit deployment and GitHub integration

---

# 🔮 Future Scope

* Real-time airline analytics integration
* Deep learning-based forecasting
* Customer churn prediction
* Route recommendation systems
* Cloud-scale analytics infrastructure
* Advanced operational intelligence modules

---

# 📌 Conclusion

The project successfully integrated analytics, business intelligence, machine learning, and deployment into a unified airline booking analytics ecosystem.

The solution enables:

* Revenue forecasting
* Operational intelligence
* Interactive analytics
* Business decision support
* Predictive business intelligence

using data-driven insights.

---

# 👨‍💻 Author

## Mohammed Zubair

Engineering Graduate | Data Analytics & Machine Learning Enthusiast

---

# ⭐ If you found this project useful, give it a star on GitHub!
