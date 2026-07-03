import streamlit as st
import time

# Progress Bar
st.write("progress bar :")
prog=st.progress(0)

for i in range(100):
    time.sleep(0.004)
    prog.progress(i+1)

# Spinner
with st.spinner("Loading..."):
    time.sleep(5)
st.success("Done")

# Success Message
st.success("form submited...",icon="✅")

# Error Message
st.error("Invalid input",icon="🚨")

# Warning
st.warning("check again",icon="⚠️")

# Info
st.info("Information",icon="ℹ️")



