#!/usr/bin/env python
import os
from dotenv import load_dotenv
from learning_assistant.crew import LearningAssistant

def run():
    """Run the Learning Assistant crew."""
    try:
        # Load environment variables
        load_dotenv()
        
        print("🚀 Initializing Learning Assistant...")
        
        # Get user input
        topic = input("\n📚 What topic would you like to learn? ")
        hours_per_week = int(input("⏱️  How many hours per week can you dedicate to learning? "))
        weeks = int(input("📅 How many weeks would you like to study this topic? "))
        
        # Initialize the crew
        learning_assistant = LearningAssistant()
        
        # Create inputs for the crew
        inputs = {
            'topic': topic,
            'hours_per_week': hours_per_week,
            'weeks': weeks,
            'difficulty': 'beginner'  # Could be made configurable
        }
        
        print("\n🧠 Creating your personalized learning plan...")
        
        # Run the crew
        crew = learning_assistant.crew()
        result = crew.kickoff(inputs=inputs)
        
        print("\n✅ Learning plan created successfully!")
        print("📂 Check the generated files in the current directory.")
        
        return result
        
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    run()
