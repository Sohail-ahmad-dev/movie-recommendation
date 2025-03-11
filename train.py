import pandas as pd

# Load dataset
movies_file = "https://files.grouplens.org/datasets/movielens/ml-100k/u.item"
ratings_file = "https://files.grouplens.org/datasets/movielens/ml-100k/u.data"

# Define column names
movie_columns = ['item_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL', 'unknown', 'Action',
                'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
                'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

rating_columns = ['user_id', 'item_id', 'rating', 'timestamp']

# Load movie data
movies = pd.read_csv(movies_file, sep='|', names=movie_columns, encoding='latin-1', usecols=range(24))
ratings = pd.read_csv(ratings_file, sep='\t', names=rating_columns)

# Merge ratings with movie details
df = pd.merge(ratings, movies, on='item_id')

# Remove unnecessary columns
df = df.drop(columns=['release_date', 'video_release_date', 'IMDb_URL', 'unknown'])

# Function to recommend top movies based on genre
def recommend_movies_by_genre(genre, top_n=10):
    if genre not in movies.columns:
        print("\n❌ Invalid genre! Please enter a valid genre from the list below.\n")
        print(list(movies.columns[5:]))  # Show available genres
        return

    # Filter movies that belong to the selected genre
    genre_movies = df[df[genre] == 1]

    # Compute average rating per movie
    top_movies = (genre_movies.groupby(['item_id', 'title'])
                  .agg({'rating': 'mean', 'user_id': 'count'})  # Average rating + Number of ratings
                  .reset_index())

    # Only consider movies with at least 50 ratings (to remove unpopular ones)
    top_movies = top_movies[top_movies['user_id'] >= 50]

    # Sort by highest average rating
    top_movies = top_movies.sort_values(by='rating', ascending=False).head(top_n)

    if top_movies.empty:
        print(f"\n❌ No highly-rated movies found in the '{genre}' genre.")
    else:
        print(f"\n🎬 **Top {top_n} Movies in '{genre}' Genre**:")
        print(top_movies[['title', 'rating', 'user_id']].rename(columns={'user_id': 'Total Ratings'}))

# Ask user for genre input
print("\n📢 Available Genres: ", list(movies.columns[5:]))
user_genre = input("\nEnter a genre (e.g., Action, Thriller, Comedy): ").strip().capitalize()

# Recommend movies based on genre
recommend_movies_by_genre(user_genre)
