import streamlit as st
import string
from annotated_text import annotated_text


# Create list of n-grams
def get_n_grams(phrase, n):
  clean_phrase = "".join( [i for i in phrase if i not in string.punctuation] )
  # return a triple: n-gram start, n-gram stop, n-gram
  return [(i, i+n, clean_phrase.split(" ")[i:i + n]) for i in range(len(phrase.split(' ') ) - n)]

# Returns list of n-grams for article and summary
def get_article_and_summary_n_grams(art, sum, n=2):
  return get_n_grams(art.lower(), n), get_n_grams(sum.lower(), n)

# Returns list of n-grams in both, with value of n first.
# I only need the ngrams from the summary that are also in the source.
def compare_n_grams(art, sum, N=2):
  A, B = get_article_and_summary_n_grams(art, sum, n=N)
  # return the tuples with start, stop and n-gram if the n-gram from the summary is also in the source text.
  summary_tuples = [i for i in B if i[2] in [j[2] for j in A]]   
  article_tuples = [j for j in A if j[2] in [k[2] for k in summary_tuples]]
  return [(p[0],m[0],p[2]) for p,m in zip(summary_tuples, article_tuples)]



l,c,r = st.columns([1,2,1])

c.title("n-gram analysis")
col1, col2, col3 = st.columns([1.5, 1, 1.5])

col1.subheader("Article")
col3.subheader("Summary")

# Right now I am getting the number of n-grams in the summary that are also in the source.
with st.form("Entry"):
  article = col1.text_input("Enter article: ")
  summary = col3.text_input("Enter summary: ")
  grams = st.slider("Select a value for n", 2, 30 )
  submit = st.form_submit_button("Select")
  if submit:
    # Display non-overlapping n-grams from summary found in original  
    # common_n_grams is a list of the above start,stop,ngram tuples.
    common_n_grams = compare_n_grams(article, summary, N=grams)[::grams]
    st.subheader(f"{len(common_n_grams)} found.")
   # st.write(common_n_grams)
    article_list = article.split(" ")
    summary_list = summary.split(" ")
    #indices = [(i[0],i[1]) for i in common_n_grams]
    #common_n_grams = [i[2] for i in common_n_grams]
   #  # c_n_grams contains the grams, indices contains start and stop index for each.
    annotated_summary = list()
    
    start = 0
    for ngram_tuple in common_n_grams:
      # add text from start to next tuple start
      annotated_summary.append(" ".join(summary_list[start:ngram_tuple[0]]))
      annotated_summary.append((" ".join(summary_list[ngram_tuple[0]:ngram_tuple[0]+grams]), '', '#fea'))
      start = ngram_tuple[0]+grams
    annotated_summary.append(" ".join(summary_list[start:]))
    
    annotated_article = list()
    
    start = 0
    for ngram_tuple in common_n_grams:
      # add text from start to next tuple start
      annotated_article.append(" ".join(article_list[start:ngram_tuple[1]]))
      annotated_article.append((" ".join(article_list[ngram_tuple[1]:ngram_tuple[1]+grams]), '', '#afa'))
      start = ngram_tuple[1]+grams
    annotated_article.append(" ".join(article_list[start:]))
    
    
    
    if len(common_n_grams) > 0:
      art_col, sum_col = st.columns(2)
      with art_col:
        st.subheader("Original:")
        annotated_text(*annotated_article)
      with sum_col:
        st.subheader("Summary:")
        annotated_text(*annotated_summary)

