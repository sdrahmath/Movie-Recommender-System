import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=ef78ace896bbff0250e7da70c9d4b34a&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def fetch_movie_details(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=ef78ace896bbff0250e7da70c9d4b34a&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    return data


def recommend(movie, num_recommendations):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        recommended_movie_details = []
        for i in distances[1:num_recommendations + 1]:
            # fetch the movie poster and details
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)
            recommended_movie_details.append(fetch_movie_details(movie_id))

        return recommended_movie_names, recommended_movie_posters, recommended_movie_details
    except IndexError:
        st.error("Movie not found. Please try another movie.")


st.set_page_config(page_title='Movie Recommender App', layout='wide')

st.markdown("""
    <div style="display: flex; align-items: center;">
        <h1 style="font-size: 45px; margin-right: -20px;">Movie Recommender App</h1>
        <h3 style="font-size: 20px; font-style:italic">(Discover Your Next Favorite Movie)</h3>
    </div>
    """, unsafe_allow_html=True)

movies = pickle.load(
    open('C:/Users/SYED AZIZ AHMED/Downloads/movie-recommender-system/movie_list.pkl', 'rb'))
similarity = pickle.load(
    open('C:/Users/SYED AZIZ AHMED/Downloads/movie-recommender-system/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("**Select or Enter a Movie**", movie_list)

num_recommendations = st.slider("**Choose Number of Recommendations:**", min_value=1, max_value=15, value=5)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters, recommended_movie_details = recommend(selected_movie,
                                                                                              num_recommendations)

    if recommended_movie_names is not None:
        cols = st.columns(5)
        for i in range(num_recommendations):
            with cols[i % 5]:
                st.markdown(recommended_movie_names[i])
                st.image(recommended_movie_posters[i], use_column_width=True)
                st.markdown("**Release Year:**")
                st.write(recommended_movie_details[i]['release_date'][:4])
                st.markdown("**Genre:**")
                st.write(', '.join([genre['name'] for genre in recommended_movie_details[i]['genres']]))
                st.markdown("**Rating:**")
                st.write(recommended_movie_details[i]['vote_average'])
