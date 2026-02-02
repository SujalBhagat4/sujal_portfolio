import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Sujal | AI & Data Analyst",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Load files
html = Path("index.html").read_text()
css = Path("style.css").read_text()

# Inject CSS
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Render HTML
st.components.v1.html(
    html,
    height=6500,
    scrolling=True
)
