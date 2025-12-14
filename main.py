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
# Hide Streamlit UI
# --------------------------------------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
iframe {
    border: none;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Load HTML safely
# --------------------------------------------------
HTML_FILE = "main.html"

if not os.path.exists(HTML_FILE):
    st.error("❌ main.html not found in project root.")
else:
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    st.components.v1.html(
        html,
        height=2300,
        scrolling=True
    )

