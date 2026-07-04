import streamlit as st


# Slider
age=st.slider("age",1,100,25)
st.write("age is",age)

# Select Box
city=st.selectbox("city",['rajkot','morbi','surat'],index=None,placeholder="select city",accept_new_options=True)
st.write("city :",city)

# Radio Button
gender=st.radio("Gender : ",['Male','Female'],index=None)
if gender:
    st.write("Gender :",gender)

# Checkbox
agree=st.checkbox("Accept Terms")
if agree:
    st.write("Great!")

# Multi Select
color=st.multiselect("select your favorite colors",['red','green','blue','yellow'],default='red',max_selections=2,placeholder="select colors",accept_new_options=True)
st.write("your favorite colors :",color)

# Button
btn=st.button("submit")
if btn:
    st.success("form submited...",icon="✅")

left, middle, right = st.columns(3)
if left.button("Plain button", width="stretch"):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", width="stretch"):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", width="stretch"):
    right.markdown("You clicked the Material button.")

# Toggle
tg = st.toggle("Dark Mode", value=False)

if tg:
    st.write("Dark Mode")
    st.markdown(f"""
    <style>
    .stApp {{
    background-color: black;
    color: white;
    }}
</style>
""", unsafe_allow_html=True)
else:
    st.write("Light Mode")




