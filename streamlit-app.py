import streamlit as st


# Create list of n-grams
def get_n_grams(phrase, n):
  return [phrase.split(" ")[i:i + n] for i in range(len(phrase.split(' ') ) -n +1 )]

# Returns list of n-grams for article and summary
def get_article_and_summary_n_grams(art, sum, n=2):
  return get_n_grams(art, n), get_n_grams(sum, n)

# Returns list of n-grams in both, with value of n first.
# I only need the ngrams from the summary that are also in the source.
def compare_n_grams(art, sum, N=2):
  A, B = get_article_and_summary_n_grams(art, sum, n=N)
  return [i for i in B if i in A]    ##  previous start of expression.  

l,c,r = st.columns([1,2,1])

c.title("n-gram analysis")
col1, col2, col3 = st.columns([1.5, 1, 1.5])

col1.subheader("Article")
col3.subheader("Summary")

# Right now I am getting the number of n-grams in the summary that are also in the source.
with st.form("Entry"):
  article = col1.text_input("Enter article: ")
  summary = col3.text_input("Enter summary: ")
  grams = st.slider("Select a value for n", 2, 16 )
  submit = st.form_submit_button("Select")
  if submit:
    # Display non-overlapping n-grams from summary found in original    ## Are there edge cases this is eliminating incorrectly?
    common_n_grams = compare_n_grams(article, summary, N=grams)[::grams]
    st.subheader(f"{len(common_n_grams)} found.")
    if len(common_n_grams) > 0:
      st.write(common_n_grams)

st.button("Reset")
    




