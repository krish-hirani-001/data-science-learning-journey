import streamlit as st

#1. Title
st.title("Student Details")

#2. Header
st.header("Data Science")

#3. Subheader
st.subheader("Machine Learning")

#4. Text
st.text("hello")

#5. Write
st.write("hello")
st.write(100)
st.write([1,2,3])

#6. Markdown
st.markdown("# heading")
st.markdown("**bold**")
st.markdown("*italic*")

#7. Code
st.code("""
for i in range(1,10)
    print(i)
""")


