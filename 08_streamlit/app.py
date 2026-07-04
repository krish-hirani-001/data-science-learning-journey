import streamlit as st

st.set_page_config(
    page_title="Streamlit Learning",
    page_icon="🐍",
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

# ---------------- Home ----------------

if page == "1. User Input 00":

    st.title("Welcome to Streamlit")
    exec(open("User_Input_00.py",encoding="utf-8").read())
    

# ---------------- Page 1 ----------------

elif page == "2. User Input 01":
    exec(open("User_Input_01.py",encoding="utf-8").read())

# ---------------- Page 2 ----------------

elif page == "3. User Input 02":
    exec(open("User_Input_02.py",encoding="utf-8").read())

# ---------------- Page 3 ----------------

elif page == "4. User Input 03":
    exec(open("User_Input_03.py",encoding="utf-8").read())

# ---------------- Page 4 ----------------

elif page == "5. User Input 04":
    exec(open("User_Input_04.py",encoding="utf-8").read())

# ---------------- Page 5 ----------------

elif page == "6. User Input 05":
    exec(open("User_Input_05.py",encoding="utf-8").read())

elif page == "7. User Input 06":
    exec(open("User_Input_06.py",encoding="utf-8").read())