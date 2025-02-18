from langchain.document_loaders import PyPDFLoader

def retrieve_event_info(query: str):
    loader = PyPDFLoader("data/temp.pdf") # later replace with actual file 
    pages = loader.load()
    # semantic serching
    relevant_content = None
    return relevant_content