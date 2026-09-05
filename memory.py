from agno.agent import Agent
from dotenv import load_dotenv
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb



load_dotenv()
db=SqliteDb(db_file="travel_assistant.db")
db.clear_memories()


def build_agent():
    

    agent=Agent(
        model=Groq(id="openai/gpt-oss-20b"),
        db=db,
        markdown=True,
        add_history_to_context=True,
        enable_agentic_memory=True,
        
        )

    return agent


groq_agent = build_agent()
groq_agent.print_response("what is capital of AUSTRALIA?")
groq_agent.print_response(
    "What is best time to visit?"
)