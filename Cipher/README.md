# Cipher Agent

[![Python CI](https://github.com/yourusername/Agents-with-crewai/actions/workflows/python-ci.yml/badge.svg)](https://github.com/yourusername/Agents-with-crewai/actions/workflows/python-ci.yml)

Cipher is a CrewAI agent for:
- Fetching Google reviews for a place
- Performing sentiment analysis
- Extracting pros and cons
- Generating a business improvement plan

## Project Structure
```
Cipher/
├── src/
│   └── cipher/
│       ├── __init__.py
│       ├── cipher_agent.py
│       ├── google_reviews.py
│       ├── improvement_plan.py
│       ├── pros_cons.py
│       └── sentiment.py
├── tests/
│   └── test_cipher_agent.py
├── examples/
│   └── example_usage.py
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .env
├── README.md
```

## Installation
1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -e .
   ```
3. **Set up your `.env` file:**
   - Copy `.env.example` to `.env` and add your Google API key:
     ```env
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage Example
Run the example script:
```bash
python examples/example_usage.py
```
This will fetch reviews, analyze sentiment, extract pros and cons, and print a business improvement plan.

## Testing
Run all tests with:
```bash
python -m unittest discover tests
```

## Continuous Integration
This project uses GitHub Actions to run tests automatically on every push or pull request to `main`.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

### To contribute:
1. Fork the repo and create your branch from `main`.
2. Install dependencies and activate your environment.
3. Add your feature or fix.
4. Add or update tests as needed.
5. Run all tests and linting.
6. Submit a pull request.

## License
[MIT](LICENSE)
