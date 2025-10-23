import streamlit as st
import pandas as pd

csv_path = "restaurant_final_risk_classification (5).csv"
df = pd.read_csv(csv_path)

risk_order = {"High Risk": 1, "Medium Risk": 2, "Low Risk": 3}
df['Risk_Rank'] = df['Category'].map(risk_order).fillna(99)
cities = df['City'].unique()[:5]

st.set_page_config(page_title="SafeBite Restaurant Risk", page_icon="🍽", layout="wide")

# Top header & team details
st.markdown(
    """
    <div style="text-align:center;">
      <h1 style='color:#673AB7;'>🍽 SafeBite Restaurant Risk Dashboard</h1>
      <div style='font-size:20px; color:#333;'>
        By <b>Chiranjith</b> | Team: <b>LoneWolf</b> | Team No: <b>A6</b>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<hr>", unsafe_allow_html=True)

# Resources/Links section
st.markdown(
    """
    <div style="background-color:#e3f2fd;padding:1rem;border-radius:8px;">
      <b>🔗 Project Resources:</b><br>
      💻 <a href="https://colab.research.google.com/drive/1doBHSL_tcRLhVpY4rpxTO8gkjMD96LR9?usp=sharing" target="_blank" style="color:#1565C0;text-decoration:underline;">Colab Model Notebook (Zero-Shot Classification)</a><br>
      🛠️ <a href="https://github.com/Chiranjith18/reviewscraper.git" target="_blank" style="color:#1565C0;text-decoration:underline;">Review Scraper (Selenium, Java) Repository</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# City selector
st.subheader("Select a city to view ranked restaurant risk:")
selected_city = st.selectbox("City", options=cities)

st.write(f"### Showing risk info for **{selected_city}** 🏙️")

city_df = df[df['City'] == selected_city].copy().sort_values('Risk_Rank')

# Restaurant count badge
st.markdown(f"<span style='font-size:18px;color:#1976D2;'>Found <b>{len(city_df)}</b> restaurants in <b>{selected_city}</b></span>", unsafe_allow_html=True)

def color_risk(val):
    if 'high' in str(val).lower():
        return 'background-color: #C62828; color: white; font-weight: bold'
    elif 'medium' in str(val).lower():
        return 'background-color: #FF9800; color: black; font-weight: bold'
    elif 'low' in str(val).lower():
        return 'background-color: #2E7D32; color: white; font-weight: bold'
    return ''

st.markdown("<br><b style='font-size:18px'>🏆 Risk Ranked Restaurants</b>", unsafe_allow_html=True)
st.dataframe(
    city_df[['Restaurant', 'Category']].style.map(color_risk, subset=['Category']),
    height=520,
    use_container_width=True
)

st.markdown(
    "<hr><p style='text-align:center; font-size:14px;'>Made for <b>HACK IT ON'25</b> | SafeBite by LoneWolf (Chiranjith)</p>", 
    unsafe_allow_html=True
)
