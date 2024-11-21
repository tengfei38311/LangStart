import sys
import os

from tools.create_md_files_retriever_tool import create_md_files_retriever_tool
from tools.create_search_engine_tool import create_search_engine_tool
from tools.create_url_retriever_tool import create_url_retriever_tools

import os

def create_tools():
    """Creates and returns all tools by combining specific tool creation methods."""

    # Get the path to the 'app_data' folder, relative to the current file's directory
    app_data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app_data")

    # Print or use the app_data_folder path
    url_retriever_tool = create_url_retriever_tools(app_data_folder)
    md_files_tool = create_md_files_retriever_tool(app_data_folder)
    search_engine_tool = create_search_engine_tool()

    tools = url_retriever_tool + [md_files_tool, search_engine_tool]
    return tools
