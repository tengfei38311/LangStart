import sys
import os

from src.tools.create_md_files_retriever_tool import create_md_files_retriever_tools
from src.tools.create_search_engine_tool import create_search_engine_tool
from src.tools.create_url_retriever_tool import create_url_retriever_tools

import os

def create_tools(app_data_folder):
    """Creates and returns all tools by combining specific tool creation methods."""

    # Print or use the app_data_folder path
    search_engine_tool = create_search_engine_tool()
    url_retriever_tool = create_url_retriever_tools(app_data_folder)
    md_files_tools = create_md_files_retriever_tools(app_data_folder)

    # tools = url_retriever_tool + md_files_tools + [search_engine_tool]
    tools = [search_engine_tool]
    tools += url_retriever_tool
    tools += md_files_tools
    return tools
