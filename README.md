🎬 Movie Recommendation System
A Flask API + Bootstrap Frontend that allows users to search movies based on: ✅ Movie Title
✅ Rating Range (0-5)
✅ Genres (Action, Thriller, Comedy, etc.)

🚀 Live Demo: Frontend | API

📌 Features
✅ Fast Flask API (Preprocessed Data for Speed)
✅ AJAX-Based Search (No Page Reloads)
✅ Bootstrap UI for Easy Filtering
✅ Free Deployment on Render (Backend) + GitHub Pages (Frontend)

📂 Project Structure
php
Copy
Edit
📁 movie-recommendation
│── 📁 static         # Frontend (HTML, CSS, Bootstrap, JS)
│   ├── index.html   # Main UI
│── 📁 ml-32m        # MovieLens 32M Dataset
│   ├── ratings.csv  # User Ratings
│   ├── movies.csv   # Movie Metadata
│── preprocess.py    # Prepares and Saves Preprocessed Data
│── app.py           # Flask API
│── requirements.txt # Dependencies
│── README.md        # Documentation
🚀 Setup & Run Locally


1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Preprocess Dataset (First Time Only)
python preprocess.py

3️⃣ Run Flask API
python app.py

API will run at: http://127.0.0.1:5000/
