import streamlit as st
import pandas as pd

# Load your datasets (Replace with actual file paths)
@st.cache_data
def load_data():
    movies = pd.read_csv("movie.csv",low_memory= False)
    tags = pd.read_csv("tag.csv", low_memory= False)
    #ratings = pd.read_csv(r"C:\Users\haris\Desktop\vs_code\IMDB_data_analysis\rating.csv", low_memory=False)
    return movies, tags  #, ratings

# Load datasets
movies, tags = load_data()

# Streamlit UI
st.title("IMDB Movie Data analysis")

# Subheaders before checkboxes
st.subheader("This IMDB dataset contains 2 tables: Movies, Tags")
st.subheader("Select any checkbox below to display the records:")

# Checkboxes to select which dataset to display
show_movies = st.checkbox("Show Movies Dataset")
show_tags = st.checkbox("Show Tags Dataset")
#show_ratings = st.checkbox("Show Ratings Dataset")

# Slider for selecting the number of records to display (Max 30)
num_records = st.slider("Select number of records to display:", min_value=0,max_value=30)

# Display datasets based on selection
if show_movies:
    st.subheader("Movies Dataset")
    st.dataframe(movies.head(num_records))

if show_tags:
    st.subheader("Tags Dataset")
    st.dataframe(tags.head(num_records))

#if show_ratings:
    #st.subheader("Ratings Dataset")
    #st.dataframe(ratings.head(num_records))
