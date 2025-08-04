# Agents with CrewAI

A collection of AI agent implementations using the CrewAI framework, showcasing different use cases and capabilities.

## 📦 Projects

### 1. Learning Assistant

An AI-powered learning companion that creates personalized learning paths, recommends resources, and generates practice exercises.

**Features:**
- Personalized learning plans based on available time
- Curated learning resources
- Practice exercise generation
- Interactive command-line interface

[View Project](./learning_assistant/README.md)

### 2. Spark - Business Opportunity Identifier

Identifies and analyzes business opportunities in specific markets.

**Features:**
- Market trend analysis
- Competitive landscape assessment
- Business opportunity identification

[View Project](./spark/README.md)

## 🛠️ Setup

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd "Agents with crewai"
```

2. Set up a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# On Windows: .venv\Scripts\activate
```

3. Install dependencies for a specific project:

```bash
cd project_name  # e.g., learning_assistant or spark
pip install -r requirements.txt
```

## 🚀 Quick Start

### Learning Assistant

```bash
cd learning_assistant
pip install -e .
python -m learning_assistant.main
```

### Spark

```bash
cd spark
pip install -e .
crewai run
```

## 📂 Project Structure

```
Agents with crewai/
├── learning_assistant/    # AI-powered learning companion
│   ├── src/               # Source code
│   ├── requirements.txt   # Dependencies
│   └── README.md          # Project documentation
├── spark/                # Business opportunity identifier
│   ├── src/               # Source code
│   ├── requirements.txt   # Dependencies
│   └── README.md          # Project documentation
└── .venv/                # Virtual environment (not version controlled)
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://www.crewai.com/) - For the amazing multi-agent framework
- [OpenAI](https://openai.com/) - For powerful language models
- [Gemini](https://ai.google/discover/gemini/) - For alternative AI models
- All contributors and open-source maintainers

## 📝 Repository Summary

The Agents-with-crewai repository is a comprehensive collection of AI agent implementations built using the CrewAI framework, designed to demonstrate various multi-agent AI use cases and collaborative capabilities. This repository contains **five main projects**, each showcasing different applications of AI agents working together to solve complex problems.

### **Key Projects Overview:**

1. **Cipher Agent** - A business intelligence agent that fetches Google reviews, performs sentiment analysis, extracts pros/cons, and generates business improvement plans. Features full CI/CD with GitHub Actions and comprehensive testing.

2. **Learning Assistant** - An AI-powered educational companion that creates personalized learning paths, curates resources, and generates practice exercises based on available study time and topics.

3. **Spark** - A business opportunity identifier that analyzes market trends, assesses competitive landscapes, and identifies potential business opportunities in specific markets.

4. **Agent123** - A foundational CrewAI template project that serves as a multi-agent system blueprint, featuring configurable agents and tasks for research and report generation.

### **Technical Architecture:**
- **Framework**: Built on CrewAI for multi-agent orchestration
- **Language**: 100% Python codebase
- **Dependencies**: Core dependencies include crewai>=0.1.0, pysbd, pytest, black, isort, and mypy
- **Structure**: Each project is self-contained with its own source code, requirements, documentation, and configuration files
- **Development**: Comprehensive testing infrastructure, CI/CD pipelines, and development tools for code quality

### **Repository Features:**
- **Modular Design**: Each agent project is independently deployable and configurable
- **Comprehensive Documentation**: Detailed README files for each project with setup and usage instructions  
- **Development Ready**: Virtual environment support, dependency management, and standardized project structure
- **Production Features**: GitHub Actions workflows, automated testing, and proper error handling
- **Extensible**: Template-based approach allows easy creation of new agent types and use cases

This repository serves as both a learning resource for CrewAI development and a production-ready foundation for building sophisticated multi-agent AI systems across various domains including business intelligence, education, market research, and more.
