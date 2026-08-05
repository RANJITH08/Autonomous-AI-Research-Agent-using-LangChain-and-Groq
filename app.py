from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_classic.agents import (create_react_agent,AgentExecutor)
from tools import tools
from prompt import prompt


# LOAD ENVIRONMENT
load_dotenv()


groq_api = os.getenv("groq_api")


if not groq_api:
    raise ValueError(
        "Groq API key not found. Check your .env file."
    )


# LLM CONFIGURATION
llm = ChatGroq(

    groq_api_key=groq_api,

    # Use bigger model when available
    model="llama-3.3-70b-versatile",

    temperature=0.1
)


# CREATE RESEARCH AGENT
agent = create_react_agent(

    llm=llm,
    tools=tools,
    prompt=prompt
)


# AGENT EXECUTOR
agent_executor = AgentExecutor(

    agent=agent,
    tools=tools,
    verbose=True,

    # allow multiple research steps
    max_iterations=8,

    # recover from formatting mistakes
    handle_parsing_errors=(
        "Invalid format. "
        "Follow ReAct format exactly."
    ),

    # stop safely
    early_stopping_method="force"
)




# USER INPUT
query = input(
    "\nEnter your research topic: "
)



# RUN AGENT
response = agent_executor.invoke(
    {
        "input": query
    }
)



# FINAL OUTPUT
print("\n")
print("=" * 70)
print("FINAL REPORT STATUS")
print("=" * 70)


print(
    response["output"]
)