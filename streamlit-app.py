import streamlit as st

l,c,r = st.columns([1,2,1])

c.title("Text Analyzer..")
col1, col2, col3 = st.columns([1.5, 1, 1.5])

col1.subheader("Article")
col3.subheader("Summary")
