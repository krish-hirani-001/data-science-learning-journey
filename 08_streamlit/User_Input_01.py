import streamlit as st

# Text Input
name=st.text_input("enter your name :")

# Password
password=st.text_input("enter password :",type="password",max_chars=8)

# Text Area
address=st.text_area("enter your address :",height=10)

# Number Input
age=st.number_input("enter your age",min_value=0,max_value=100,step=1)


st.write("")
st.write("your name is :",name)
st.write("your age is :",age)
st.write("your password is :",password)
st.write(f"address :{address}")





