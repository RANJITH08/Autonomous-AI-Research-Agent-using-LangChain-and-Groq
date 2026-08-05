from langchain_core.tools import tool

from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun

from pathlib import Path
import re



# WIKIPEDIA TOOL
wiki = WikipediaAPIWrapper(
    top_k_results=5,
    doc_content_chars_max=5000
)


@tool
def wikipedia_search(query: str) -> str:
    """
    Search Wikipedia for research information.
    """

    try:

        result = wiki.run(query)

        return f"""
SOURCE:
Wikipedia

CONTENT:

{result}
"""

    except Exception as e:

        return f"""
Wikipedia failed.

Error:
{str(e)}
"""


# WEB SEARCH TOOL
duck = DuckDuckGoSearchRun()


@tool
def web_search(query: str) -> str:
    """
    Search web information.
    """

    try:

        result = duck.run(query)

        return f"""
SOURCE:
Web Search

CONTENT:

{result}
"""

    except Exception as e:

        return f"""
Web search failed.

Error:
{str(e)}
"""


# SAVE TOOL
@tool
def save_research(report: str) -> str:
    """
    Save the complete research paper into a file.

    Input:
    Complete research paper text.
    """

    try:

        folder = Path("research_reports")

        folder.mkdir(exist_ok=True)

        title = "Research_Report"

        if "TITLE:" in report:

            title = (
                report
                .split("TITLE:")[1]
                .split("\n")[0]
                .strip()
            )

        filename = re.sub(
            r'[^a-zA-Z0-9_]',
            '_',
            title
        )

        filepath = folder / f"{filename}.txt"
        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(report)
        return (
            f"Research saved successfully: {filepath}"
        )


    except Exception as e:

        return (
            f"Save failed: {str(e)}"
        )


# EXPORT TOOLS
tools = [
    wikipedia_search,
    web_search,
    save_research
]