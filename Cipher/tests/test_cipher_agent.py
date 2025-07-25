import unittest
from src.cipher.cipher_agent import CipherAgent

class TestCipherAgent(unittest.TestCase):
    def setUp(self):
        self.agent = CipherAgent()

    def test_fetch_google_reviews(self):
        # This test should mock GoogleReviewsFetcher for offline testing
        self.assertTrue(hasattr(self.agent, 'fetch_google_reviews'))

    def test_analyze_sentiment(self):
        reviews = [{'text': 'Great service!'}, {'text': 'Terrible experience.'}]
        analyzed = self.agent.analyze_sentiment(reviews)
        self.assertIsInstance(analyzed, list)
        self.assertTrue(all('polarity' in r for r in analyzed))

    def test_extract_pros_cons(self):
        analyzed = [
            {'text': 'Great!', 'polarity': 0.8},
            {'text': 'Bad.', 'polarity': -0.9}
        ]
        pros, cons = self.agent.extract_pros_cons(analyzed)
        self.assertIn('Great!', pros)
        self.assertIn('Bad.', cons)

    def test_generate_improvement_plan(self):
        pros = ['Clean rooms']
        cons = ['Slow service']
        plan = self.agent.generate_improvement_plan(pros, cons)
        self.assertIn('Clean rooms', plan)
        self.assertIn('Slow service', plan)

if __name__ == '__main__':
    unittest.main()
