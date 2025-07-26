from crewai import Agent

class CipherAgent(Agent):
    """
    Cipher agent for fetching Google reviews, performing sentiment analysis,
    extracting pros/cons, and generating business improvement plans.
    """
    
    def __init__(self, llm=None):
        super().__init__(
            role="Business Review Analyst",
            goal="Analyze Google reviews to extract insights and generate business improvement recommendations",
            backstory="""You are an expert business analyst specializing in customer feedback analysis. 
            You have extensive experience in sentiment analysis, extracting actionable insights from reviews, 
            and creating data-driven improvement plans for businesses.""",
            llm=llm
        )
    def fetch_google_reviews(self, place_name: str, api_key: str, num_reviews: int = 20):
        """
        Fetch Google reviews for a given place using Google Places API.
        """
        from google_reviews import GoogleReviewsFetcher
        place_id = GoogleReviewsFetcher.fetch_place_id(place_name, api_key)
        reviews = GoogleReviewsFetcher.fetch_reviews(place_id, api_key, num_reviews)
        return reviews

    def analyze_sentiment(self, reviews: list):
        """
        Perform sentiment analysis on the list of reviews.
        Returns a list of dicts with sentiment scores and text.
        """
        from sentiment import SentimentAnalyzer
        return SentimentAnalyzer.analyze_reviews(reviews)

    def extract_pros_cons(self, analyzed_reviews: list):
        """
        Extract pros and cons from analyzed reviews.
        Returns two lists: pros and cons.
        """
        from pros_cons import ProsConsExtractor
        return ProsConsExtractor.extract(analyzed_reviews)

    def generate_improvement_plan(self, pros: list, cons: list):
        """
        Generate a business improvement plan based on pros and cons.
        Returns a string or structured plan.
        """
        from improvement_plan import ImprovementPlanner
        return ImprovementPlanner.generate_plan(pros, cons)
