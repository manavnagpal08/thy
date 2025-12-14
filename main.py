
import streamlit as st
import os

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="ScreenerPro • AI Hiring Platform",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# Hide Streamlit Default UI
# --------------------------------------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Load main.html
# --------------------------------------------------
HTML_FILE = "main.html"

if not os.path.exists(HTML_FILE):
    st.error("❌ main.html not found. Please add it to the project root.")
else:
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html_content = f.read()

    st.components.v1.html(
        html_content,
        height=2200,
        scrolling=True
    )
