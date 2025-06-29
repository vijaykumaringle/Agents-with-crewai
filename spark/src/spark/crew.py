from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Spark():
    """Spark - Business Opportunity Identifier for Pune"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def demographic_analyst(self) -> Agent:
        """Expert in analyzing population data and consumer behavior for Pune"""
        return Agent(
            config={
                "name": "Demographic Analyst",
                "description": "Expert in analyzing population data, income levels, and consumer behavior for Pune",
                "tools": {
                    "web_search": {
                        "description": "Search the web for demographic data and local surveys",
                        "type": "function"
                    },
                    "data_visualization": {
                        "description": "Create visualizations of demographic data",
                        "type": "function"
                    }
                }
            },
            verbose=True
        )

    @agent
    def market_trend_researcher(self) -> Agent:
        """Identifies emerging consumer trends and industry shifts in Pune"""
        return Agent(
            config={
                "name": "Market Trend Researcher",
                "description": "Identifies emerging consumer trends and industry shifts in Pune",
                "tools": {
                    "web_search": {
                        "description": "Search news and industry reports",
                        "type": "function"
                    },
                    "news_api": {
                        "description": "Access local and national news",
                        "type": "function"
                    }
                }
            },
            verbose=True
        )

    @agent
    def competitor_analyst(self) -> Agent:
        """Specializes in competitive intelligence for Pune businesses"""
        return Agent(
            config={
                "name": "Competitor Analyst",
                "description": "Analyzes existing businesses and market competition in Pune",
                "tools": {
                    "web_search": {
                        "description": "Search Google Maps and local business directories",
                        "type": "function"
                    },
                    "review_analysis": {
                        "description": "Analyze customer reviews and ratings",
                        "type": "function"
                    }
                }
            },
            verbose=True
        )

    @agent
    def opportunity_synthesizer(self) -> Agent:
        """Business strategist for identifying opportunities in Pune"""
        return Agent(
            config={
                "name": "Opportunity Synthesizer",
                "description": "Analyzes all gathered data to identify business opportunities in Pune",
                "tools": {}
            },
            verbose=True
        )

    @task
    def demographic_analysis_task(self) -> Task:
        """Task for demographic data collection and analysis"""
        return Task(
            config={
                "name": "Demographic Analysis",
                "description": "Collect and analyze demographic data for Pune",
                "dependencies": [],
                "output_file": "demographics_report.md"
            }
        )

    @task
    def market_trends_task(self) -> Task:
        """Task for market trend research"""
        return Task(
            config={
                "name": "Market Trends Analysis",
                "description": "Research local and national market trends affecting Pune",
                "dependencies": [],
                "output_file": "market_trends_report.md"
            }
        )

    @task
    def competition_analysis_task(self) -> Task:
        """Task for competitive analysis"""
        return Task(
            config={
                "name": "Competitive Analysis",
                "description": "Analyze existing businesses and competition in Pune",
                "dependencies": [],
                "output_file": "competition_report.md"
            }
        )

    @task
    def opportunity_identification_task(self) -> Task:
        """Task for synthesizing data and identifying opportunities"""
        return Task(
            config={
                "name": "Opportunity Identification",
                "description": "Synthesize all data to identify business opportunities in Pune",
                "dependencies": [
                    "demographic_analysis_task",
                    "market_trends_task",
                    "competition_analysis_task"
                ],
                "output_file": "business_opportunities_report.md"
            }
        )

    @crew
    def run(self) -> None:
        """Run the Spark crew"""
        pass

    @crew
    def crew(self) -> Crew:
        """Creates the Spark crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
