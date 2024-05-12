from pydantic import BaseModel

class PostModel(BaseModel):
    name: str
    content: str