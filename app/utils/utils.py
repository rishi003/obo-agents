import os
from app.config import Config

def get_root_input_dir(id: str):
    """Get the local root input directory for file based on id."""
    root_dir =  os.getcwd()
    docs_dir = Config.DOCS_DIR
    root_docs_dir = os.path.join(root_dir, docs_dir, id)
    if not os.path.exists(root_docs_dir):
        os.makedirs(root_docs_dir)
    return root_docs_dir
    