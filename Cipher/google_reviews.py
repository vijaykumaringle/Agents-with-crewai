import requests
from typing import List, Dict
import os

class GoogleReviewsFetcher:
    """
    Fetches Google reviews for a place using Google Places API (v1, 2025).
    """
    PLACES_SEARCH_URL = "https://places.googleapis.com/v1/places:searchText"
    PLACE_DETAILS_URL = "https://places.googleapis.com/v1/places/{}"

    @staticmethod
    def fetch_place_id(place_name: str, api_key: str) -> str:
        headers = {
            "X-Goog-Api-Key": api_key,
            "X-Goog-FieldMask": "places.id,places.displayName"
        }
        data = {
            "textQuery": place_name
        }
        resp = requests.post(GoogleReviewsFetcher.PLACES_SEARCH_URL, headers=headers, json=data)
        result = resp.json()
        print("DEBUG: New Places API searchText response:", result)
        places = result.get("places", [])
        if places:
            return places[0]["id"]
        raise ValueError(f"No place_id found for {place_name}")

    @staticmethod
    def fetch_reviews(place_id: str, api_key: str, num_reviews: int = 20) -> List[Dict]:
        url = GoogleReviewsFetcher.PLACE_DETAILS_URL.format(place_id)
        headers = {
            "X-Goog-Api-Key": api_key,
            # Request only the reviews field for efficiency
            "X-Goog-FieldMask": "reviews"
        }
        resp = requests.get(url, headers=headers)
        result = resp.json()
        print("DEBUG: New Places API details response:", result)
        reviews = result.get("reviews", [])
        return reviews[:num_reviews]
