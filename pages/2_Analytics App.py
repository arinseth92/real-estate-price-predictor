import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Plotting Demo")
st.title("Analytics App")

# Load data
new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))

# Geomap
group_df = new_df.groupby('sector')[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']].mean().reset_index()
st.header('Sector Price per Sqft Geomap')
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                        color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                        mapbox_style="open-street-map", width=100, height=800, hover_name="sector")
st.plotly_chart(fig, use_container_width=True)

# Wordcloud with filter
st.header("Features Wordcloud")

# New dropdown to filter wordcloud by property type
wordcloud_property_type = st.selectbox('Select Property Type for WordCloud', ['overall', 'flat', 'house'])

if wordcloud_property_type == 'overall':
    text_data = feature_text
else:
    # You must ensure your dataframe has a 'features' or equivalent column for each row
    filtered_df = new_df[new_df['property_type'] == wordcloud_property_type]
    if 'features' in filtered_df.columns:
        text_data = ' '.join(filtered_df['features'].dropna().astype(str).tolist())
    else:
        text_data = feature_text  # fallback if 'features' column not found

# Generate wordcloud
wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=set(['s']),
                      min_font_size=10).generate(text_data)
fig_wc = plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
st.pyplot(fig_wc)

# Area vs Price
st.header('Area vs Price')
property_type = st.selectbox('Select Property Type for Price Chart', ['flat', 'house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

st.plotly_chart(fig1, use_container_width=True)

st.header('BHK Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(new_df, names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)

st.header('Side by Side BHK price comparison')

fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)


st.header('Side by Side Distplot for property type')

fig3 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)

