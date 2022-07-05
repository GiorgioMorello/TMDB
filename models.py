from enum import Enum
from typing import List
from datetime import datetime
from dataclasses import dataclass

@dataclass
class OriginalLanguage(Enum):
    EN = "en"
    ES = "es"

@dataclass
class Movie:
    adult: bool
    backdrop_path: str
    genre_ids: List[int]
    id: int
    original_language: OriginalLanguage
    original_title: str
    overview: str
    popularity: float
    poster_path: str
    release_date: datetime
    title: str
    video: bool
    vote_average: float
    vote_count: int

    def __init__(self, adult: bool, backdrop_path: str, genre_ids: List[int], id: int, original_language: OriginalLanguage, original_title: str, overview: str, popularity: float, poster_path: str, release_date: datetime, title: str, video: bool, vote_average: float, vote_count: int) -> None:
        self.adult = adult
        self.backdrop_path = backdrop_path
        self.genre_ids = genre_ids
        self.id = id
        self.original_language = original_language
        self.original_title = original_title
        self.overview = overview
        self.popularity = popularity
        self.poster_path = poster_path
        self.release_date = release_date
        self.title = title
        self.video = video
        self.vote_average = vote_average
        self.vote_count = vote_count

@dataclass
class DiscoverMovieResponse:
    page: int
    results: List[Movie]
    total_pages: int
    total_results: int

    def __init__(self, page: int, results: List[Movie], total_pages: int, total_results: int) -> None:
        self.page = page
        self.results = results
        self.total_pages = total_pages
        self.total_results = total_results
