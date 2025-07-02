from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.tools import tool
from typing import List, Dict, Any

# Import tools from tools.py
from spark.tools.tools import (
    web_search,
    news_api,
    review_analysis,
    data_visualization
)
@CrewBase
class Spark():
    """Spark - Business Opportunity Identifier for Pune"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def demographic_analyst(self) -> Agent:
        """Expert in analyzing population data and consumer behavior for Pune"""
        return Agent(
            role="Demographic Analyst",
            goal="Analyze population data, income levels, and consumer behavior for Pune to identify business opportunities",
            backstory="""You are an expert in demographic analysis with years of experience in understanding population 
            trends and consumer behavior. Your insights help businesses understand their target markets and make 
            data-driven decisions.""",
            tools=[web_search, data_visualization],
            verbose=True
        )

    @agent
    def market_trend_researcher(self) -> Agent:
        """Identifies emerging consumer trends and industry shifts in Pune"""
        return Agent(
            role="Market Trend Researcher",
            goal="Identify and analyze emerging market trends and industry shifts in Pune",
            backstory="""You are a seasoned market researcher with a keen eye for spotting trends before they go mainstream. 
            Your ability to analyze market data and predict shifts helps businesses stay ahead of the curve.""",
            tools=[web_search, news_api],
            verbose=True
        )

    @agent
    def competitor_analyst(self) -> Agent:
        """Specializes in competitive intelligence for Pune businesses"""
        return Agent(
            role="Competitor Analyst",
            goal="Analyze competitors and market landscape in Pune to identify opportunities and threats",
            backstory="""You are a competitive intelligence expert who specializes in analyzing competitors and market 
            dynamics. Your insights help businesses understand their competitive landscape and find opportunities for 
            differentiation.""",
            tools=[web_search, review_analysis],
            verbose=True
        )

    @agent
    def opportunity_synthesizer(self) -> Agent:
        """Business strategist for identifying opportunities in Pune"""
        return Agent(
            role="Opportunity Synthesizer",
            goal="Synthesize data from all sources to identify the most promising business opportunities in Pune",
            backstory="""You are a strategic thinker with a talent for identifying business opportunities. 
            You analyze data from various sources to spot patterns and opportunities that others might miss. 
            Your insights help entrepreneurs and businesses make informed decisions about new ventures.""",
            tools=[web_search, news_api, review_analysis, data_visualization],
            verbose=True
        )

    @task
    def demographic_analysis_task(self) -> Task:
        """Task for demographic data collection and analysis"""
        return Task(
            description="""
            Collect and analyze demographic data for Pune including:
            - Population statistics
            - Income levels
            - Age distribution
            - Education levels
            - Consumer behavior patterns
            
            Your analysis should identify key demographic trends and their implications for business opportunities.
            """,
            expected_output="A comprehensive report on Pune's demographics and their business implications",
            agent=self.demographic_analyst(),
            tools=[web_search, data_visualization],
            output_file="demographics_report.md"
        )

    @task
    def market_trends_task(self) -> Task:
        """Task for market trend research"""
        return Task(
            description="""
            Research and analyze current market trends in Pune including:
            - Emerging consumer preferences
            - Industry growth sectors
            - Economic indicators
            - Technological advancements
            - Government policies affecting business
            
            Focus on identifying trends that present new business opportunities.
            """,
            expected_output="A detailed analysis of current market trends in Pune with a focus on business opportunities",
            agent=self.market_trend_researcher(),
            tools=[web_search, news_api],
            output_file="market_trends_report.md"
        )

    @task
    def competition_analysis_task(self) -> Task:
        """Task for competitive analysis"""
        return Task(
            description="""
            Analyze the competitive landscape in Pune including:
            - Major competitors in key industries
            - Market gaps and underserved segments
            - Competitive advantages of existing businesses
            - Customer reviews and feedback
            - Pricing strategies
            
            Identify areas where new businesses could compete effectively.
            """,
            expected_output="A comprehensive competitive analysis report highlighting market gaps and opportunities",
            agent=self.competitor_analyst(),
            tools=[web_search, review_analysis],
            output_file="competition_report.md"
        )

    @task
    def opportunity_identification_task(self) -> Task:
        """Task for synthesizing data and identifying opportunities"""
        return Task(
            description="""
            Synthesize the data from all research to identify the most promising business opportunities in Pune.
            Consider:
            - Market demand
            - Competition
            - Growth potential
            - Resource requirements
            - Risk factors
            
            Prioritize opportunities based on feasibility and potential return on investment.
            """,
            expected_output="A prioritized list of business opportunities in Pune with detailed analysis of each",
            agent=self.opportunity_synthesizer(),
            context=[
                self.demographic_analysis_task(),
                self.market_trends_task(),
                self.competition_analysis_task()
            ],
            tools=[web_search, news_api, review_analysis, data_visualization],
            output_file="business_opportunities_report.md"
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
            tools=[web_search, news_api, review_analysis, data_visualization],
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
