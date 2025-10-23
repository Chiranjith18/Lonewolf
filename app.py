import streamlit as st
import pandas as pd

csv_path = "restaurant_final_risk_classification (5).csv"
df = pd.read_csv(csv_path)

risk_order = {"High Risk": 1, "Medium Risk": 2, "Low Risk": 3}
df['Risk_Rank'] = df['Category'].map(risk_order).fillna(99)
cities = df['City'].unique()[:5]

st.set_page_config(page_title="SafeBite Risk Dashboard", page_icon="🍽", layout="wide")

st.markdown(
    """
    <style>
    .main {background-color: #f4f7fb;}
    .block-container {padding-top: 2rem;}
    </style>
    """,
    unsafe_allow_html=True
)

# Title box
st.markdown(
    "<h1 style='text-align:center; color:#2C3E50;'>🍽 Restaurant Risk Dashboard</h1>", 
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; font-size:20px;'>by <b>Chiranjith</b> | Team: <b>LoneWolf</b> | Team No: <b>A6</b></p>", 
    unsafe_allow_html=True
)

st.markdown("<hr>", unsafe_allow_html=True)

# City selector with dropdown for better UX
st.subheader("Select a city to view ranked restaurant risk:")
selected_city = st.selectbox("City", options=cities)

st.write(f"### Showing risk info for **{selected_city}** :cityscape:")

city_df = df[df['City'] == selected_city].copy().sort_values('Risk_Rank')

# Add count stats
st.info(f"Found {len(city_df)} restaurants in {selected_city}")

# Risk color styling for DataFrame
def color_risk(val):
    if 'high' in str(val).lower():
        color = 'red'
    elif 'medium' in str(val).lower():
        color = 'orange'
    elif 'low' in str(val).lower():
        color = 'green'
    else:
        color = 'grey'
    return f'background-color: {color}; color: white; font-weight: bold'

# Display DataFrame in wider columns with colored categories
st.markdown("#### 🏆 Top Risk Restaurants (sorted)")
st.dataframe(
    city_df[['Restaurant', 'Category']].style.map(color_risk, subset=['Category']),
    height=500,
    use_container_width=True
)

# Optional: Add a little footer
st.markdown(
    "<hr><p style='text-align:center; font-size:14px;'>Made for HACK IT ON'25 - By LoneWolf (Chiranjith)</p>", 
    unsafe_allow_html=True
)
