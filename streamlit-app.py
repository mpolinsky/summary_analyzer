import streamlit as st

# Returns list of n-grams in both, with value of n first.
def compare_n_grams(A, B, n=2):
  return (n, [i for i in list(A.ngrams(n)) if i in list(B.ngrams(n))] if len(list(A.ngrams(n=2))) > len(list(B.ngrams(n))) else [i for i in list(B.ngrams(n)) if i in list(A.ngrams(n=2))])


l,c,r = st.columns([1,2,1])

c.title("Text Analyzer..")
col1, col2, col3 = st.columns([1.5, 1, 1.5])

col1.subheader("Article")
col3.subheader("Summary")

with st.form("Entry"):
  article = col1.text_input("Enter article: ")
  summary = col3.text_input("Enter summary: ")
  N = st.slider("Pick a value for n-grams", 0, len(summary.split(" . "))-1 )
  submit = st.form_submit_button("Select")
  if submit:
    compare_n_grams(article, summary, n=N)
    #col1.write(article)
    #col3.write(summary)

st.button("Reset")
    
st.subheader("End")



