from setuptools import setup, find_packages

setup(
    name="learning_assistant",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "crewai>=0.28.8",
        "python-dotenv>=1.0.0",
        "openai>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "learning-assistant=learning_assistant.main:run",
        ],
    },
)
