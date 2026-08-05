# Autonomous AI Research Agent using LangChain and Groq


## Overview

This project is an autonomous AI research assistant built using LangChain ReAct Agent architecture.

The agent can:

- Understand research queries
- Decide which tools to use
- Retrieve information from external sources
- Generate structured research papers
- Automatically save the final report into a file


The goal of this project is to demonstrate an agentic AI workflow where an LLM can reason, use tools, collect information, and complete a research task autonomously.



# Architecture


User Query

↓

LangChain ReAct Agent

↓

Groq Llama LLM

↓

Tool Selection Layer

↓

├── Wikipedia Research Tool

├── Web Search Tool

└── Save Research Tool

↓

Research Processing

↓

Academic Research Report

↓

File Storage



# Features


## Autonomous Research

The AI agent decides the research workflow automatically using the ReAct framework.


## Multiple Knowledge Sources

The agent uses:

- Wikipedia API for trusted background information
- Web search as a fallback source


## Academic Report Generation

The generated report contains:


- Title
- Abstract
- Introduction
- History and Development
- Main Content
- Applications
- Advantages
- Limitations
- Future Scope
- Conclusion
- References


## Automatic File Saving

Research papers are automatically stored:

```
research_reports/
      topic_name.txt
```



# Technologies Used


| Technology | Purpose |
|-|-|
| Python | Programming Language |
| LangChain | AI Agent Framework |
| ReAct Agent | Reasoning Workflow |
| Groq LLM | Language Model |
| Wikipedia API | Knowledge Retrieval |
| DuckDuckGo Search | Web Search |
| Prompt Engineering | Agent Control |



# Project Structure


```
wikipedia_researching_ai_agent/

│
├── app.py
│
├── tools.py
│
├── prompt.py
│
├── requirements.txt
│
├── .env.example
│
├── README.md
│
├── research_reports/
│
└── .gitignore

```



# Installation


Clone repository:


```bash
git clone your_repository_link
```


Move into project:


```bash
cd wikipedia_researching_ai_agent
```


Create virtual environment:


```bash
python -m venv research_env
```


Activate environment:


Windows:

```bash
research_env\Scripts\activate
```



Install dependencies:


```bash
pip install -r requirements.txt
```



# Environment Setup


Create a `.env` file:


```
groq_api=YOUR_GROQ_API_KEY
```



# Running the Agent


Run:


```bash
python -m app
```


Enter your research topic:


Example:

```
History of Artificial Intelligence
```


The agent will:

1. Research information
2. Select tools
3. Generate a report
4. Save the file automatically



# Example Output


```
research_reports/

History_of_Artificial_Intelligence.txt

```



# Future Improvements


Planned improvements:

- PDF research paper generation
- Citation management
- Multiple document sources
- Vector database integration
- RAG architecture
- Research quality evaluation
- Web crawling capability



# Learning Outcomes


This project demonstrates:

- Agentic AI development
- LangChain tool calling
- Prompt engineering
- LLM orchestration
- Autonomous workflows
- AI automation design



# Author

Ranjith N

AI Engineering Portfolio Project
