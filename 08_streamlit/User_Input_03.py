import streamlit as st
import pandas as pd
import datetime
from pathlib import Path


# File Upload
file=st.file_uploader("upload",accept_multiple_files=True,type=["jpg", "png"])
for i in file:
    st.image(i)

read_csv=st.file_uploader("upload",accept_multiple_files=True,type="csv")
for j in read_csv:
    df=pd.read_csv(j)
    st.write(df) 
    
# Date Picker
a=datetime.date(2026,2,1)
b=datetime.date(2026,6,18)
date=st.date_input("DOB",format="DD/MM/YYYY",min_value=a,max_value=b)
st.write("Selected Date is : ",date.strftime("%d/%m/%Y"))

# Color Picker
color=st.color_picker("select color")
st.write("The current color is", color)

# Display Images
BASE_DIR = Path(__file__).parent

st.image(BASE_DIR / "veldora.png", caption="veldora technology", width=400)

# Display Video
# vecteezy_4k-animation-clip-data-analysis-statistical-for-business_46578851
st.video(str(BASE_DIR / "videos.mp4"),loop=True,autoplay=True,muted=True)

# Display Audio
st.audio(str(BASE_DIR / "music.mp3"),loop=True,autoplay=True)




