import pandas as pd

ratings_file = "ml-32m/ratings.csv"
movies_file = "ml-32m/movies.csv"

print("Loading data...")

ratings = pd.read_csv(ratings_file)
movies = pd.read_csv(movies_file)

df = pd.merge(ratings, movies, on="movieId")

df["genres"] = df["genres"].apply(lambda x: x.split("|"))

movie_ratings = df.groupby("movieId").agg({"rating": "mean", "title": "first", "genres": "first", "userId": "count"}).reset_index()

movie_ratings = movie_ratings[movie_ratings["userId"] >= 50]

movie_ratings = movie_ratings.sort_values(by="rating", ascending=False)

movie_ratings.to_pickle("preprocessed_movies.pkl")

print("Preprocessed data saved! Run Flask API now.")
