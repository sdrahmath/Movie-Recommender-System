# Movie Recommender System

This project is a movie recommendation app based on a content-based machine learning algorithm. The app suggests similar movies based on the selected movie's attributes such as genre, release year, and rating.

# Content-Based Learning in Machine Learning

Content-based learning in machine learning refers to a method of recommendation or information retrieval that focuses on the characteristics or attributes of the items being recommended. This approach is commonly used in recommender systems, where the goal is to suggest items to users based on their preferences.

## How it Works

The content-based learning algorithm follows these steps:

1. Extract and represent the features of each item in a numerical or vector form.
2. Calculate the similarity between items using measures like cosine similarity.
3. Use user preferences or input to identify items that match their preferences.
4. Provide recommendations based on the similarity of item features.

## Example: Movie Recommendation System

In a movie recommendation system, the content-based approach can be applied as follows:

1. Extract features of movies, such as genre, actors, directors, and plot keywords.
2. Represent each movie as a feature vector based on these attributes.
3. Calculate the similarity between movies using cosine similarity or other distance measures.
4. When a user expresses their preferences, identify movies with similar features.
5. Recommend movies that have similar actors, genres, or other relevant attributes.

By leveraging the content or features of movies, the content-based approach can suggest personalized movie recommendations based on user preferences.

## Advantages

Content-based learning offers several advantages, including:

- Ability to recommend new or unpopular items.
- Handling the cold-start problem with new users.
- Independence from historical user data.

## Limitations

While content-based learning has its strengths, it also has some limitations:

- Reliance on the availability and quality of item features.
- Difficulty capturing complex user preferences.
- Potential challenges in discovering unexpected recommendations.


## Description of the Project

The Movie Recommender System utilizes a content-based approach, where movies are recommended based on their similarity to the selected movie. The similarity is calculated using features such as genre, release year, and rating. The app fetches movie data from The Movie Database (TMDb) API and uses the dataset to generate recommendations.

## Technologies and Tools

The following technologies and tools were used in the development of this project:

- Python
- Pandas
- NumPy
- Pickle
- Requests
- PyCharm
- Jupyter Notebook
- Streamlit

## Dataset

The dataset used in this project was obtained from Kaggle. It was generated from The Movie Database (TMDb) API, which provides access to a vast collection of movie data, including information about movies, actors, crew members, and TV shows. You can find more information about the dataset and access it on Kaggle: [Kaggle Dataset - Movie Recommender System](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

## Output Screenshot

![Output Screenshot](https://github.com/sdrahmath/Movie-Recommender-System/blob/main/output/output.png)



The screenshot above shows a sample output of the movie recommendation app. It displays the selected movie, along with the top recommended movies, including their posters, titles, release years, genres, ratings, and brief plot summaries.


## Output GIF

![Output GIF](https://github.com/sdrahmath/Movie-Recommender-System/blob/main/output/output.gif)



The above GIF demonstrates the functionality of the movie recommendation app. Users can select a movie and click the "Show Recommendation" button to receive a list of recommended movies based on their selection.

## Acknowledgements

This dataset was generated from The Movie Database (TMDb) API. The project utilizes the TMDb API to fetch movie data but is not endorsed or certified by TMDb. The TMDb API offers access to comprehensive movie, actor, crew, and TV show information. You can explore the TMDb API [here](https://www.themoviedb.org/documentation/api).

