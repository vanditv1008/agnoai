from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.groq import Groq


def build_agent():
    load_dotenv()

    agent=Agent(
        model=Groq(id="openai/gpt-oss-20b"),
        tools=[DuckDuckGoTools()],
        instructions="You are a helpful travel assistant.",
        add_datetime_to_context=True,  
        )

    return agent


groq_agent = build_agent()

groq_agent.print_response(
    "Is there a war in Iran?"
)