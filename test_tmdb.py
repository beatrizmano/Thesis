import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("TMDB_API_KEY")

# One test call: details of a known film (Parasite, id 496243)
r = requests.get(
    "https://api.themoviedb.org/3/movie/496243",
    params={"api_key": key, "append_to_response": "external_ids"},
    timeout=30,
)
print(r.status_code)
d = r.json()
print(d["title"], d["release_date"], d["runtime"], d["external_ids"]["imdb_id"])

# First page of US theatrical releases in 2019
r = requests.get(
    "https://api.themoviedb.org/3/discover/movie",
    params={
        "api_key": key,
        "region": "US",
        "with_release_type": "2|3",
        "primary_release_date.gte": "2019-01-01",
        "primary_release_date.lte": "2019-12-31",
        "sort_by": "popularity.desc",
        "page": 1,
    },
    timeout=30,
)
j = r.json()
print("Total candidates in 2019:", j["total_results"], "| pages:", j["total_pages"])