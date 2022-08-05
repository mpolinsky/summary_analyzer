import streamlit as st

l,c,r = st.columns([1,2,1])

c.title("Text Analyzer..")
col1, col2, col3 = st.columns([1.5, 1, 1.5])

col1.subheader("Article")
col3.subheader("Summary")

with st.form("Entry"):
  article = col1.text_input("Enter article: ")
  summary = col2.text_input("Enter summary: ")

col1.write(article)
col2.write(summary)

st.subheader("End")



