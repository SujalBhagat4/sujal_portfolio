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

# Load HTML & CSS
html_file = Path("index.html").read_text()
css_file = Path("style.css").read_text()

st.markdown(f"<style>{css_file}</style>", unsafe_allow_html=True)
st.components.v1.html(html_file, height=4000, scrolling=True)
