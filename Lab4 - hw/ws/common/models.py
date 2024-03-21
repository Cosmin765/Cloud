from pydantic import BaseModel


class Team(BaseModel):
    name: str
    score: int
    image_url: str
    pilot_ids: list


class PilotExtraInfo(BaseModel):
    team_id: str
    country: str
    podiums: int


class Pilot(BaseModel):
    first_name: str
    last_name: str
    score: int
    image_url: str
    extra_info: PilotExtraInfo
