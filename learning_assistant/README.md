# Learning Assistant with CrewAI

A personalized learning assistant that helps you master new topics by creating customized learning paths, finding relevant resources, and generating practice exercises.

## Features

- 🎯 Personalized learning plans based on your available time
- 📚 Curated learning resources for any topic
- 💪 Practice exercises to reinforce learning
- 🗓️ Structured study schedule

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd learning_assistant
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

### Usage

Run the learning assistant:

```bash
python -m learning_assistant.main
```

Follow the prompts to:
1. Enter the topic you want to learn
2. Specify your available study time per week
3. Set your desired study duration

The assistant will generate:
- A personalized learning plan
- Curated learning resources
- Practice exercises

## Project Structure

```
learning_assistant/
├── src/
│   └── learning_assistant/
│       ├── __init__.py
│       ├── crew.py       # Crew and agent definitions
│       └── main.py       # Main entry point
├── .env.example          # Example environment variables
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
