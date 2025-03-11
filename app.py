from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd

app = Flask(__name__, static_folder="static", template_folder="static")
CORS(app)  # Allow frontend requests

print("🔄 Loading preprocessed data...")
movie_ratings = pd.read_pickle("preprocessed_movies.pkl")  # Load preprocessed file
print("✅ Data loaded!")

def search_movies(title="", min_rating=0, max_rating=5, genres=[]):
    """
    Fast search through preprocessed data.
    """
    filtered_df = movie_ratings[(movie_ratings["rating"] >= min_rating) & (movie_ratings["rating"] <= max_rating)]
    
    if title:
        filtered_df = filtered_df[filtered_df["title"].str.contains(title, case=False, na=False)]
    
    if genres:
        filtered_df = filtered_df[filtered_df["genres"].apply(lambda g_list: any(g in g_list for g in genres))]

    return filtered_df[["title", "rating", "genres"]].head(10).to_dict(orient="records")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():
    title = request.args.get("title", "")
    min_rating = float(request.args.get("min_rating", 0))
    max_rating = float(request.args.get("max_rating", 5))
    genres = request.args.get("genres", "").split(",") if request.args.get("genres") else []

    results = search_movies(title, min_rating, max_rating, genres)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
