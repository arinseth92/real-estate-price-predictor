import streamlit as st

# Page setup
st.set_page_config(page_title="🏠 Gurgaon Real Estate Price Predictor")

# Title
st.title("🏠 Real Estate Price Predictor – Gurgaon Edition")

# Description
st.markdown("""
Welcome to **Real Estate Price Predictor** – A machine learning-powered web app to estimate **property prices in Gurgaon**.

---

### 🔍 What is this app?
This web app helps you estimate real estate prices in **Gurgaon** based on features like area, location, and amenities. It also allows you to:

- 📈 **Price Prediction**: Input Gurgaon property details and get an estimated price.
- 📊 **Analytics**: Visualize data insights like area-price trends and location-based clusters.
- 🧠 **Recommender System**: Discover similar or nearby properties based on location, budget, and features.

---

### ✨ Features
- 💰 Price Prediction for: 
    - Independent Floors  
    - Independent Houses  
- 📊 Analytics Page: Explore insights from various Gurgaon localities.
- 🧭 Recommender: Suggests similar Gurgaon properties within your budget or radius.
- 📥 Download Resources: Datasets and ML models used in this project.

---

### 🛠 Tech Stack
- **Programming**: Python  
- **Data Analysis**: Pandas, NumPy  
- **Visualization**: Matplotlib, Seaborn, Plotly  
- **Machine Learning**: Scikit-learn  
- **App Framework**: Streamlit  
- **Version Control**: Git & GitHub  
- **Validation**: Pydantic  

---

### ⚙️ Installation
To run this project locally:

1. Clone this repo:
    ```bash
    git clone <your-repo-link>
    ```
2. Create a virtual environment and install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the app:
    ```bash
    streamlit run Real_Estate_Project.py
    ```

---

### 📚 Acknowledgements
- [99acres.com](https://www.99acres.com): Source of property listing data.  
- [CampusX DSMP](https://learnwith.campusx.in/t/u/activeCourses): Inspiration from their capstone structure.

---

### 📜 License
- [MIT License](https://choosealicense.com/licenses/mit/)

> **Disclaimer**: This project uses publicly available data from 99acres.com for educational purposes only. Estimates may not reflect real-time market prices.

---

💡👨‍💻 Developed by **Arin Seth**
""")
