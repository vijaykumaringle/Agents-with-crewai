import requests
from typing import List, Dict

class GoogleReviewsFetcher:
    """
    Fetches Google reviews for a place using Google Places API.
    """
    PLACES_SEARCH_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    PLACE_DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"

    @staticmethod
    def fetch_place_id(place_name: str, api_key: str) -> str:
        params = {
            "input": place_name,
            "inputtype": "textquery",
            "fields": "place_id",
            "key": api_key
        }
        resp = requests.get(GoogleReviewsFetcher.PLACES_SEARCH_URL, params=params)
        data = resp.json()
        candidates = data.get("candidates")
        if candidates:
            return candidates[0]["place_id"]
        raise ValueError(f"No place_id found for {place_name}")

    @staticmethod
    def fetch_reviews(place_id: str, api_key: str, num_reviews: int = 20) -> List[Dict]:
        params = {
            "place_id": place_id,
            "fields": "review",
            "key": api_key
        }
        resp = requests.get(GoogleReviewsFetcher.PLACE_DETAILS_URL, params=params)
        data = resp.json()
        reviews = data.get("result", {}).get("reviews", [])
        return reviews[:num_reviews]
