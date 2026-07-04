import streamlit as st
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).parent

logo = Image.open(BASE_DIR / "logo.png")

st.set_page_config(
    page_title="Streamlit Learning",
    page_icon=logo,
    layout="wide"
)

# ---------------- Sidebar ----------------

st.sidebar.title("Python Streamlit Components")

page = st.sidebar.radio(
    "Select Page",
    (
        "1. User Input 00",
        "2. User Input 01",
        "3. User Input 02",
        "4. User Input 03",
        "5. User Input 04",
        "6. User Input 05",
        "7. User Input 06",
    )
)

if page == "1. User Input 00":
    exec((BASE_DIR / "User_Input_00.py").read_text(encoding="utf-8"))

elif page == "2. User Input 01":
    exec((BASE_DIR / "User_Input_01.py").read_text(encoding="utf-8"))

elif page == "3. User Input 02":
    exec((BASE_DIR / "User_Input_02.py").read_text(encoding="utf-8"))

elif page == "4. User Input 03":
    exec((BASE_DIR / "User_Input_03.py").read_text(encoding="utf-8"))

elif page == "5. User Input 04":
    exec((BASE_DIR / "User_Input_04.py").read_text(encoding="utf-8"))

elif page == "6. User Input 05":
    exec((BASE_DIR / "User_Input_05.py").read_text(encoding="utf-8"))

elif page == "7. User Input 06":
    exec((BASE_DIR / "User_Input_06.py").read_text(encoding="utf-8"))