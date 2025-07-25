from typing import List, Dict, Tuple

class ProsConsExtractor:
    """
    Extracts pros and cons from analyzed reviews based on sentiment polarity and keywords.
    """
    @staticmethod
    def extract(analyzed_reviews: List[Dict], polarity_threshold: float = 0.2) -> Tuple[List[str], List[str]]:
        pros = []
        cons = []
        for review in analyzed_reviews:
            text = review['text']
            polarity = review['polarity']
            # If polarity is clearly positive, consider as pro
            if polarity > polarity_threshold:
                pros.append(text)
            # If polarity is clearly negative, consider as con
            elif polarity < -polarity_threshold:
                cons.append(text)
        return pros, cons
