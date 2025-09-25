# import sys
# import os

# from src.tools.create_md_files_retriever_tool import create_md_files_retriever_tools
# from src.tools.create_search_engine_tool import create_search_engine_tool
# from src.tools.create_url_retriever_tool import create_url_retriever_tools

# import os

# def create_tools(app_data_folder):
#     """Creates and returns all tools by combining specific tool creation methods."""

#     # Print or use the app_data_folder path
#     search_engine_tool = create_search_engine_tool()
#     url_retriever_tool = create_url_retriever_tools(app_data_folder)
#     md_files_tools = create_md_files_retriever_tools(app_data_folder)

#     # tools = url_retriever_tool + md_files_tools + [search_engine_tool]
#     tools = [search_engine_tool]
#     tools += url_retriever_tool
#     tools += md_files_tools
#     return tools

# =============================================
# 2024-11-24 Tony
import csv
import os

from src.tools.create_md_files_retriever_tool import create_md_files_retriever_tools
from src.tools.create_search_engine_tool import create_search_engine_tool
from src.tools.create_url_retriever_tool import create_url_retriever_tools

def read_csv_files(csv_folder):
    """Reads and processes all .csv files in the specified folder."""
    csv_data = []

    for file_name in os.listdir(csv_folder):
        if file_name.endswith('.csv'):
            file_path = os.path.join(csv_folder, file_name)
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                # Skip the header row if necessary
                header = next(reader, None)
                
                # Process rows and add to csv_data
                for row in reader:
                    csv_data.append(row)

    return csv_data

def create_tools(app_data_folder, csv_folder):
    """Creates and returns all tools by combining specific tool creation methods, including .csv handling."""

    # Create tools
    search_engine_tool = create_search_engine_tool()
    url_retriever_tool = create_url_retriever_tools(app_data_folder)
    md_files_tools = create_md_files_retriever_tools(app_data_folder)

    # Process CSV files
    csv_data = read_csv_files(csv_folder)
    
    # Example: you can pass `csv_data` to tools if needed
    print(f"Processed {len(csv_data)} rows from CSV files.")

    tools = [search_engine_tool]
    tools += url_retriever_tool
    tools += md_files_tools

    return tools

# Example usage:
# app_data_folder = "path_to_app_data"
# csv_folder = "path_to_csv_files"
# tools = create_tools(app_data_folder, csv_folder)

