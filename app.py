from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TMDB_API_KEY = os.environ.get("2b77016502908b1d4f0ed6f99e109849")

@app.route("/movie/<int:movie_id>")
def get_movie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    return jsonify(response.json())

@app.route("/search")
def search():
    query = request.args.get("query")
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={query}"
    response = requests.get(url)
    return jsonify(response.json())
