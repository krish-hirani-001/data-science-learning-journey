import pandas as pd
import streamlit as st

# Line Chart
chart = pd.DataFrame({
    "a": [1, 2, 3, 4, 5],
    "b": [2, 3, 4, 5, 6]
})

st.line_chart(chart)

# Bar Chart
df=pd.DataFrame({
    "a" : [1,2,3,4,5],
    "b" : [6,7,8,9,10]
})
st.bar_chart(df,x_label="stud mark",y_label="student", horizontal=False)

# Area Chart
st.area_chart(df)

# Scatter Chart
df=pd.DataFrame({
    "a" : [5,2,7,4,3],
    "b" : [11,7,14,21,10]
})
st.scatter_chart(df)

# Camera Input
image = st.camera_input("Take Photo")
