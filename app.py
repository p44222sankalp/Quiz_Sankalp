import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'linear_regression_model.pkl'
model = pickle.load(open(filename, 'rb'))

# Create a title for your app
st.title("Monthly Revenue Prediction App")

# Create input fields for the features
st.header("Enter Store Details:")
website_visits = st.number_input("Website Visits", min_value=0)
avg_order_value = st.number_input("Average Order Value", min_value=0.0)
customer_acquisition_cost = st.number_input("Customer Acquisition Cost", min_value=0.0)
marketing_spend = st.number_input("Marketing Spend", min_value=0.0)
number_of_products = st.number_input("Number of Products", min_value=0)

# Create a button to make predictions
if st.button("Predict Monthly Revenue"):
    # Create a DataFrame with the user input
    input_data = pd.DataFrame({
        'website_visits': [website_visits],
        'avg_order_value': [avg_order_value],
        'customer_acquisition_cost': [customer_acquisition_cost],
        'marketing_spend': [marketing_spend],
        'number_of_products': [number_of_products]
    })

    # Make predictions using the loaded model
    predicted_revenue = model.predict(input_data)[0]

    # Display the predicted revenue
    st.header("Predicted Monthly Revenue:")
    st.write(f"${predicted_revenue:.2f}")
