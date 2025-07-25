#!/usr/bin/env python
import sys
import os
from datetime import datetime

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Now import the run function from spark.main
from spark.main import run

if __name__ == "__main__":
    print("Starting Spark CrewAI agent...")
    try:
        result = run()
        if result:
            print("\nAgent execution completed successfully!")
            print(result)
        else:
            print("\nAgent completed but returned no results.")
    except Exception as e:
        print(f"Error running agent: {str(e)}", file=sys.stderr)
        sys.exit(1)
