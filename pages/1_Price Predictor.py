import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests

st.set_page_config(page_title="Viz Demo")

# Load df.pkl from Hugging Face
df_url = "https://huggingface.co/arinseth92/real-estate-models/resolve/main/df.pkl?download=true"
response = requests.get(df_url)
df = pickle.loads(response.content)

# Load pipeline.pkl from Hugging Face
pipeline_url = "https://huggingface.co/arinseth92/real-estate-models/resolve/main/pipeline.pkl?download=true"
response2 = requests.get(pipeline_url)
pipeline = pickle.loads(response2.content)

# UI
st.header('Enter your inputs')

# property_type
property_type = st.selectbox('Property Type', ['flat', 'house'])

# sector
sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
bedrooms = float(st.selectbox('Number of Bedroom', sorted(df['bedRoom'].unique().tolist())))
bathroom = float(st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))
balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))
property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))
built_up_area = float(st.number_input('Built Up Area'))
servant_room = float(st.selectbox('Servant Room', [0.0, 1.0]))
store_room = float(st.selectbox('Store Room', [0.0, 1.0]))
furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

# Predict button
if st.button('Predict'):
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area,
             servant_room, store_room, furnishing_type, luxury_category, floor_category]]

    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    one_df = pd.DataFrame(data, columns=columns)

    # Predict price
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    st.success(f"The price of the flat is between ₹ {round(low, 2)} Cr and ₹ {round(high, 2)} Cr")
