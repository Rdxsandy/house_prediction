import streamlit as st
import pickle
import pandas as pd

# load trained model
with open("house_price_gb_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="House Price Prediction", layout="centered")

st.title("🏠 House Price Prediction")

st.write("Enter house details to predict price")

area = st.number_input("Area (sqft)", min_value=500, max_value=3000, value=1500)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=5, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=4, value=2)
age = st.number_input("House Age (years)", min_value=0, max_value=40, value=10)
location = st.slider("Location Score", min_value=1, max_value=10, value=7)

if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        "area_sqft": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age": age,
        "location_score": location
    }])

    prediction = model.predict(input_df)
    st.success(f"Estimated Price: ₹ {prediction[0]:.2f} Lakhs")
