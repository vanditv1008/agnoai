from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools

def build_agent():
    load_dotenv()

    agent=Agent(
        model=Groq(id="openai/gpt-oss-20b"),
        tools=[ YFinanceTools(), DuckDuckGoTools() ],
        description="This agent is designed to answer questions about finance and stock market data.",
        add_datetime_to_context=True,
        instructions="format your response with tables showing the data and provide a summary of the data in a paragraph at the end of the response."
        )

    return agent


groq_agent = build_agent()

groq_agent.print_response(
    "share the NVDA stock price provide "
)