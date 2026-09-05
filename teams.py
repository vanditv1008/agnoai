from agno.agent import Agent
from dotenv import load_dotenv
from agno.models.groq import Groq
from agno.team import Team
from dotenv import load_dotenv

load_dotenv()

eng_agent=Agent(
  name="English Travel Assistant",
role="You are a helpful travel assistant in English.",
    
    )
hindi_agent=Agent(
    name="Hindi Travel Assistant",
    role="You are a helpful travel assistant in Hindi.",
    
    )
chine_agent=Agent(
    name="Chinese Travel Assistant",
    role="You are a helpful travel assistant in Chinese.",
    )

team=Team(
    name="Travel Assistant Team",
    members=[eng_agent, hindi_agent, chine_agent],
    model=Groq(id="openai/gpt-oss-20b"),
    markdown=True,
    instructions="all members must answer the question in respective language do not call single agent",
    show_members_responses=True,
)

team.print_response("What is capital of India?")
