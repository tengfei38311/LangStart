import sys
import os

from utilities.create_retriever_from_md_files import create_retriever_from_md_files, find_md_files
from utilities.create_retriever_from_urls import create_retriever_from_urls, load_urls

from langchain.tools.retriever import create_retriever_tool
from langchain_community.tools.tavily_search import TavilySearchResults

import os

def create_search_engine_tool():
    """Creates a Tavily search results tool."""
    return TavilySearchResults(max_results=10)
