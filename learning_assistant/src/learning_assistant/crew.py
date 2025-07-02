from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.tools import tool
from typing import List, Dict, Any

@tool
def search_learning_resources(topic: str) -> str:
    """Search for learning resources on a given topic."""
    return f"Here are some learning resources for {topic}: [Resource 1, Resource 2, Resource 3]"

@tool
def create_study_plan(topic: str, hours_per_week: int, weeks: int) -> Dict[str, Any]:
    """Create a personalized study plan based on topic, available hours, and duration."""
    return {
        "topic": topic,
        "duration_weeks": weeks,
        "weekly_hours": hours_per_week,
        "plan": f"Week-by-week breakdown for learning {topic} over {weeks} weeks, {hours_per_week} hours per week"
    }

@tool
def recommend_practice_exercises(topic: str, difficulty: str = "beginner") -> List[str]:
    """Recommend practice exercises for a given topic and difficulty level."""
    return [
        f"{difficulty.capitalize()} exercise 1 for {topic}",
        f"{difficulty.capitalize()} exercise 2 for {topic}",
        f"{difficulty.capitalize()} exercise 3 for {topic}"
    ]

@CrewBase
class LearningAssistant():
    """A crew that helps users learn new topics through personalized learning paths."""
    
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def learning_strategist(self) -> Agent:
        """Creates effective learning strategies and plans."""
        return Agent(
            role="Learning Strategist",
            goal="Create effective learning strategies and study plans",
            backstory="""You are an expert in educational psychology and learning methodologies. 
            You help learners optimize their study time and create effective learning paths.""",
            tools=[create_study_plan],
            verbose=True
        )

    @agent
    def resource_finder(self) -> Agent:
        """Finds and recommends learning resources."""
        return Agent(
            role="Resource Finder",
            goal="Find high-quality learning resources for any topic",
            backstory="""You have extensive knowledge of educational resources across various platforms 
            and can find the best materials for any learning objective.""",
            tools=[search_learning_resources],
            verbose=True
        )

    @agent
    def practice_coach(self) -> Agent:
        """Creates practice exercises and assessments."""
        return Agent(
            role="Practice Coach",
            goal="Create and recommend practice exercises to reinforce learning",
            backstory="""You are an expert in creating effective practice exercises and assessments 
            that help learners master new concepts through active engagement.""",
            tools=[recommend_practice_exercises],
            verbose=True
        )

    @task
    def create_learning_plan(self) -> Task:
        """Task to create a personalized learning plan."""
        return Task(
            description="""Create a personalized learning plan based on the user's topic, 
            available time, and learning goals.""",
            expected_output="A detailed learning plan with timeline and milestones",
            agent=self.learning_strategist(),
            output_file="learning_plan.md"
        )

    @task
    def find_resources(self) -> Task:
        """Task to find relevant learning resources."""
        return Task(
            description="Find high-quality learning resources for the user's topic",
            expected_output="A curated list of learning resources (courses, books, tutorials, etc.)",
            agent=self.resource_finder(),
            output_file="learning_resources.md"
        )

    @task
    def create_practice_exercises(self) -> Task:
        """Task to create practice exercises."""
        return Task(
            description="Create practice exercises to help the user master the topic",
            expected_output="A set of practice exercises with varying difficulty levels",
            agent=self.practice_coach(),
            output_file="practice_exercises.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Learning Assistant crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
