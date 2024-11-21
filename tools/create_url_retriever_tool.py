import os
from utilities.create_retriever_from_urls import create_retriever_from_urls, load_urls
from langchain.tools.retriever import create_retriever_tool
from langchain_community.tools.tavily_search import TavilySearchResults

def create_url_retriever_tools(app_data_folder):
    """Creates a list of retriever tools from all .urls files in the app_data/urls directory."""
    url_retriever_tools = []

    # List all files in the app_data_folder/urls directory
    urls_folder = os.path.join(app_data_folder, "urls")
    
    # Check if the directory exists
    if not os.path.exists(urls_folder):
        print(f"Directory not found: {urls_folder}")
        return url_retriever_tools

    # Iterate through all files in the urls folder
    for file_name in os.listdir(urls_folder):
        # Process only .urls files
        if file_name.endswith(".urls"):
            urls_file = os.path.join(urls_folder, file_name)
            name, description, urls = load_urls(urls_file)

            # Create the retriever tool
            url_retriever_tool = create_retriever_tool(
                retriever=create_retriever_from_urls(urls),
                name=name,
                description=description
            )
            url_retriever_tools.append(url_retriever_tool)

    return url_retriever_tools
