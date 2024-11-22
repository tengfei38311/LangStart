import os

from src.utilities.create_retriever_from_md_files import create_retriever_from_md_files, find_md_files
from langchain.tools.retriever import create_retriever_tool


def create_md_files_retriever_tools(app_data_folder):
    """Creates retriever tools for each subfolder in the docs folder."""
    docs_folder = os.path.join(app_data_folder, "docs")
    retriever_tools = []

    # Loop through each subfolder in the docs directory
    for subfolder_name in os.listdir(docs_folder):
        subfolder_path = os.path.join(docs_folder, subfolder_name)

        if os.path.isdir(subfolder_path):
            # Path to the description.txt in the subfolder
            description_file_path = os.path.join(subfolder_path, "description.txt")

            if os.path.exists(description_file_path):
                try:
                    # Read the description from description.txt with UTF-8 encoding
                    with open(description_file_path, "r", encoding="utf-8") as file:
                        description = file.read().strip()

                    # Find all markdown files in the subfolder
                    md_files = find_md_files(subfolder_path)

                    # Create the retriever tool for the current subfolder
                    md_files_tool = create_retriever_tool(
                        retriever=create_retriever_from_md_files(md_files),
                        name=subfolder_name,  # Use subfolder name as tool name
                        description=description,  # Use the description from description.txt
                    )
                    retriever_tools.append(md_files_tool)

                except UnicodeDecodeError:
                    print(f"Error decoding {description_file_path}. Skipping this folder.")
                    continue  # Skip to the next folder if there's an encoding error

    return retriever_tools
