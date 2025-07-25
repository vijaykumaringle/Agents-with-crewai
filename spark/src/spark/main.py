#!/usr/bin/env python
import os
import sys
import warnings
from datetime import datetime
from typing import Dict, Any

# Suppress warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Set up environment variables if needed
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Import the Spark crew
from .crew import Spark

def run():
    """
    Run the Spark crew for Pune business opportunity identification.
    """
    inputs = {
        'location': 'Pune',
        'current_year': str(datetime.now().year),
        'analysis_date': datetime.now().strftime('%Y-%m-%d')
    }
    
    try:
        print("Initializing Spark crew...")
        spark = Spark()
        
        print("Creating crew...")
        crew = spark.crew()
        
        print("\nStarting the Spark crew to analyze business opportunities in Pune...")
        result = crew.kickoff(inputs=inputs)
        
        print("\nCrew execution completed successfully!")
        if hasattr(crew, 'output') and crew.output:
            print(f"\nResults: {crew.output}")
        
        return result
    except Exception as e:
        print(f"Error during crew execution: {str(e)}", file=sys.stderr)
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    if len(sys.argv) < 3:
        print("Usage: crewai train <n_iterations> <output_file>")
        return
        
    inputs = {
        "topic": "Business Opportunities in Pune",
        'current_year': str(datetime.now().year)
    }
    
    try:
        print(f"Training crew for {sys.argv[1]} iterations...")
        spark = Spark()
        spark.crew().train(
            n_iterations=int(sys.argv[1]), 
            filename=sys.argv[2], 
            inputs=inputs
        )
        print(f"Training completed. Results saved to {sys.argv[2]}")
    except Exception as e:
        print(f"Error during training: {str(e)}", file=sys.stderr)
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    if len(sys.argv) < 2:
        print("Usage: crewai replay <task_id>")
        return
        
    try:
        print(f"Replaying task {sys.argv[1]}...")
        spark = Spark()
        spark.crew().replay(task_id=sys.argv[1])
        print("Replay completed successfully.")
    except Exception as e:
        print(f"Error during replay: {str(e)}", file=sys.stderr)
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "Business Opportunities in Pune",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Spark().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
