import pandas as pd

# Load dataset
ratings_file = "ml-32m/ratings.csv"
movies_file = "ml-32m/movies.csv"

print("🔄 Loading data...")

# Read CSV files
ratings = pd.read_csv(ratings_file)
movies = pd.read_csv(movies_file)

# Merge ratings with movie details
df = pd.merge(ratings, movies, on="movieId")

# Convert genre column into a list
df["genres"] = df["genres"].apply(lambda x: x.split("|"))

# Compute the average rating per movie
movie_ratings = df.groupby("movieId").agg({"rating": "mean", "title": "first", "genres": "first", "userId": "count"}).reset_index()

# Keep only movies with at least 50 ratings
movie_ratings = movie_ratings[movie_ratings["userId"] >= 50]

# Sort by rating
movie_ratings = movie_ratings.sort_values(by="rating", ascending=False)

# Save the preprocessed file
movie_ratings.to_pickle("preprocessed_movies.pkl")

print("✅ Preprocessed data saved! Run Flask API now.")
