from pydantic import BaseModel, Field


class Document(BaseModel):
    """Interface for interacting with a document."""

    page_content: str = None
    metadata: dict = Field(default_factory=dict)

    def __init__(self, page_content, metadata, *args, **kwargs):
        super().__init__(page_content=page_content, metadata=metadata, *args, **kwargs)