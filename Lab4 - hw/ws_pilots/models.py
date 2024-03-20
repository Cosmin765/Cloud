from pydantic import BaseModel


class PilotExtraInfo(BaseModel):
    team: str
    country: str
    podiums: int


class Pilot(BaseModel):
    first_name: str
    last_name: str
    score: int
    image_url: str
    extra_info: PilotExtraInfo
