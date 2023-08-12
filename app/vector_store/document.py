from pydantic import BaseModel, Field


class Document(BaseModel):
    """Interface for interacting with a document."""

    page_content: str = None
    metadata: dict = Field(default_factory=dict)

    def __init__(self, page_content, *args, **kwargs):
        super().__init__(text_content=page_content, *args, **kwargs)