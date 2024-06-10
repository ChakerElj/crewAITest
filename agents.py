from crewai import Agent
from textwrap import dedent
from langchain.llms import AzureOpenAI, Ollama
import os
from langchain_openai import AzureChatOpenAI


class TravelAgents:
    def __init__(self):
        self.AzureOpenAIGPT35 = AzureChatOpenAI(azure_deployment="ai-ser-openai",
                                                openai_api_version="2023-06-01-preview",azure_endpoint="https://ai-ser-us.openai.azure.com/")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics. i have decades of 
            experience making travel iteneraries"""),
            goal=dedent(f"""
            create a 7-day travel itinerary with detailed per-day plans,
            include budget , packing suggestions, and safety tips.
            """),
            allow_delegation=False,
            verbose=True,
            llm=self.AzureOpenAIGPT35
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert at analyzing travel data to pick ideal destinations"""),
            goal=dedent(f"""select the cities based on weather , season , prices , and traveler interests"""),
            allow_delegation=False,
            verbose=True,
            llm=self.AzureOpenAIGPT35

        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information 
            about the city , it's attractions and customs"""),
            goal=dedent(f"""Provide the BEST insights about the selected cities"""),
            allow_delegation=False,
            verbose=True,
            llm=self.AzureOpenAIGPT35
        )
