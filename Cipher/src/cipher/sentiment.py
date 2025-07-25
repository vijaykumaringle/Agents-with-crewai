from textblob import TextBlob
from typing import List, Dict

class SentimentAnalyzer:
    """
    Analyzes sentiment of reviews using TextBlob.
    """
    @staticmethod
    def analyze_reviews(reviews: List[dict]) -> List[Dict]:
        results = []
        for review in reviews:
            text = review.get('text') or review.get('reviewText') or ''
            if not text:
                continue
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity
            results.append({
                'text': text,
                'author': review.get('author_name', ''),
                'rating': review.get('rating', None),
                'polarity': polarity,
                'subjectivity': subjectivity
            })
        return results
