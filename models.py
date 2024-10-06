from pydantic import BaseModel
from typing import List

class Preferences(BaseModel):
    desired_roles: List[str]
    locations: List[str]
    job_type: str

class UserProfile(BaseModel):
    name: str
    skills: List[str]
    experience_level: str
    preferences: Preferences
