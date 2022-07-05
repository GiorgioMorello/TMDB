import requests
import json
from flask import Flask, jsonify
from IPython import embed
from os import getenv
from models import DiscoverMovieResponse, Movie 
from typing import List


TMDB_BASE_API = "https://api.themoviedb.org/3"
API_KEY = getenv("API_KEY")

def get_trending_movies(api_key) -> List[Movie]:
    discover_route = f"{TMDB_BASE_API}/discover/movie?sort_by=popularity.desc&api_key={api_key}"
    result = requests.get(discover_route)
    discover_movie = DiscoverMovieResponse(**result.json())
    return discover_movie.results


movies = get_trending_movies(API_KEY)


app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify([m for m in movies])
