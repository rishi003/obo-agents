import os
from app.tests.test_summarizer import test_summarize
from app.tests.test_vector_store import test_hf_emb, test_chroma, test_chroma_deletion
from app.tests.test_document_loader import test_doc_loader
from app.utils.utils import get_root_input_dir

if __name__ == "__main__":
    # test_summarize()

    # print(get_root_input_dir("test"))

    # test_hf_emb()

    test_chroma()

    # test_chroma_deletion()

    # test_doc_loader()
