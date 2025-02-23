from pydantic import BaseModel
from datetime import datetime


class ArtImage(BaseModel):
    id: str
    url: str
    embeddings: list
    metadata: dict
    created_at: datetime


class Metadata(BaseModel):
    artist: str
    size: str
    extracted_features: dict  # like saturation, etc..
    tags: list
    prompt: str




