from pydantic import BaseModel


class Pilot(BaseModel):
    first_name: str
    last_name: str
    score: int
