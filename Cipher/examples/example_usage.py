import os
from src.cipher.cipher_agent import CipherAgent

def main():
    # Set your Google Places API key here
    api_key = os.getenv('GOOGLE_API_KEY') or 'YOUR_API_KEY_HERE'
    place_name = "Taj Mahal Hotel Mumbai"  # Example place
    num_reviews = 10

    agent = CipherAgent()
    print(f"Fetching reviews for: {place_name}")
    reviews = agent.fetch_google_reviews(place_name, api_key, num_reviews)
    print(f"Fetched {len(reviews)} reviews.")

    print("\nAnalyzing sentiment...")
    analyzed = agent.analyze_sentiment(reviews)

    print("\nExtracting pros and cons...")
    pros, cons = agent.extract_pros_cons(analyzed)

    print("\nGenerating improvement plan...")
    plan = agent.generate_improvement_plan(pros, cons)
    print(plan)

if __name__ == "__main__":
    main()
