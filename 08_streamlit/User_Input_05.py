import streamlit as st

# Columns
co1,co2,co3=st.columns(3)
with co1:
    st.write("left")
with co2:
    st.write("center")
with co3:
    st.write("right")

#Sidebar
st.sidebar.title("Menu")

option = st.sidebar.selectbox(
    "Choose",
    ["Home","About"]
)

# Expander
with st.expander("More Info"):
    st.write("Hidden Text")

# Tabs
tab1,tab2 = st.tabs(
    ["Home","About"]
)

with tab1:
    st.write("Home")

with tab2:
    st.write("About")

# metric
st.metric(
    "Revenue",
    "₹50,000",
    "+10%"
)