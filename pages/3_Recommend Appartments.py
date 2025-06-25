import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests

st.set_page_config(page_title="Recommend Apartments")

# Load all required .pkl files from Hugging Face
def load_pickle_from_url(url):
    response = requests.get(url)
    return pickle.loads(response.content)

location_df = load_pickle_from_url("https://huggingface.co/arinseth92/real-estate-models/resolve/main/location_distance.pkl?download=true")
cosine_sim1 = load_pickle_from_url("https://huggingface.co/arinseth92/real-estate-models/resolve/main/cosine_sim1.pkl?download=true")
cosine_sim2 = load_pickle_from_url("https://huggingface.co/arinseth92/real-estate-models/resolve/main/cosine_sim2.pkl?download=true")
cosine_sim3 = load_pickle_from_url("https://huggingface.co/arinseth92/real-estate-models/resolve/main/cosine_sim3.pkl?download=true")

# Recommender function
def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]
    top_properties = location_df.index[top_indices].tolist()
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })
    return recommendations_df

# UI
st.title('Select Location and Radius')

selected_location = st.selectbox('Location', sorted(location_df.columns.to_list()))
radius = st.number_input('Radius in Kms')

if st.button('Search'):
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()
    for key, value in result_ser.items():
        st.text(str(key) + " — " + str(round(value / 1000)) + ' kms')

st.title('Recommend Apartments')

selected_apartment = st.selectbox('Select an apartment', sorted(location_df.index.to_list()))

if st.button('Recommend'):
    recommendation_df = recommend_properties_with_scores(selected_apartment)
    st.dataframe(recommendation_df)

