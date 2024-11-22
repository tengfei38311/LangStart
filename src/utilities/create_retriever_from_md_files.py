import os
from pathlib import Path
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_openai.embeddings import OpenAIEmbeddings


def create_retriever_from_md_files(md_files):
    """
    Create a retriever using the content from markdown files.
    """
    if not md_files:
        print("Warning: No markdown files provided to create the retriever.")
        return None

    # Parse markdown content into sections using file paths
    sections = []
    for md_file in md_files:
        sections += parse_markdown(md_file)  # Pass the file path instead of content

    if not sections:
        print("Warning: No sections were parsed from the markdown files.")
        return None

    # sections = [
    #     "我们公司的前台叫小丽。",
    #     "公司附近国贸三期楼下的烤鱼很好吃。",
    #     "你的直属领导是张经理。",
    #     "请事假需要提前一天向直属领导提交申请。病假无需提前请假，可以于事后向直属领导补办，但需要有医院的就诊记录。",
    # ]

    # Create a vector store and retriever
    vectorstore = DocArrayInMemorySearch.from_texts(
        sections,
        embedding=OpenAIEmbeddings(),
    )
    retriever = vectorstore.as_retriever()
    return retriever

def find_md_files(md_path):
    """
    Find markdown (.md) files given a path.
    If the path is a folder, return a list of absolute paths of all .md files in it.
    If the path is a file ending with .md, return a list with its absolute path.
    If the path is invalid or does not contain .md files, return an empty list and print a warning.
    """
    md_files = []

    # Check if the path exists
    if not os.path.exists(md_path):
        print(f"Warning: The path does not exist: {md_path}")
        return md_files

    path_obj = Path(md_path)

    # If the path is a directory, find all .md files
    if path_obj.is_dir():
        md_files = [str(file.resolve()) for file in path_obj.glob("*.md")]
        if not md_files:
            print(f"Warning: No markdown files found in the folder: {md_path}")
    # If the path is a file and ends with .md, return its absolute path
    elif path_obj.is_file() and path_obj.suffix == ".md":
        md_files = [str(path_obj.resolve())]
    else:
        print(f"Warning: The path is not a valid folder or markdown file: {md_path}")

    return md_files

def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    sections = []
    title_stack = []
    current_content = []

    for line in lines:
        if line.startswith('#'):
            # Found a title, determine its level
            level = len(line.split()[0])
            title = line.strip().split(' ', 1)[1]

            # Update the title stack to reflect the current title hierarchy
            if level <= len(title_stack):
                title_stack = title_stack[:level-1]
            title_stack.append(title)

            # Save the previous section if it exists
            if current_content:
                sections.append("\n".join(current_content))
                current_content = []

            # Start a new section with the hierarchical title
            hierarchical_title = " - ".join(title_stack)
            current_content.append(hierarchical_title)

        else:
            # Accumulate content for the current section
            current_content.append(line.strip())

    # Add the last section if any content is remaining
    if current_content:
        sections.append("\n".join(current_content))

    return sections


# # Example usage
# if __name__ == "__main__":
#     # Load the API key from the .env file
#     load_dotenv(find_dotenv())

#     # Path to the folder or file
#     md_folder_or_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app_data")

#     # Load markdown files
#     md_content = load_md_files(md_folder_or_file)

#     # Create retriever
#     retriever = create_retriever_from_md_files(md_content)

#     if retriever:
#         # Example usage of the retriever
#         print("Retriever is ready to be used!")
