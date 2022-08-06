import requests
import json
from flask import Flask, jsonify, render_template
from os import getenv
from models import DiscoverMovieResponse, Movie, GenreResponse
from typing import List, Dict


TMDB_BASE_API = "https://api.themoviedb.org/3"
API_KEY = getenv("API_KEY")

def get_trending_movies(api_key) -> List[Movie]:
    discover_route = f"{TMDB_BASE_API}/discover/movie?sort_by=popularity.desc&api_key={api_key}"
    result = requests.get(discover_route)
    discover_movie = DiscoverMovieResponse(**result.json())
    return discover_movie.results


def get_genres(api_key) -> Dict[int, str]:
    genre_route = f"{TMDB_BASE_API}/genre/movie/list?api_key={api_key}"
    result = requests.get(genre_route)
    genres_response = GenreResponse(**result.json())
    return genres_response.to_dict()

def get_genre_color(id: int):
    colors = [
        "#f94144",
        "#f3722c",
        "#f8961e",
        "#f9844a",
        "#f9c74f",
        "#90be6d",
        "#43aa8b",
        "#4d908e",
        "#577590",
        "#277da1"
    ]

    position = id % len(colors)
    return colors[position]


movies = get_trending_movies(API_KEY)


app = Flask(__name__)


@app.route('/')
def main():
    movies = get_trending_movies(API_KEY)
    genres = get_genres(API_KEY)
    return render_template('index.html', movies=movies, genres=genres, get_genre_color=get_genre_color)

app.run(debug=True)
