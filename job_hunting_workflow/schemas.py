from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional, Dict

class Job(BaseModel):
    id: str
    title: str
    company: str
    location: str
    source: str  # indeed, linkedin, etc.
    url: Optional[HttpUrl]
    description: str
    tags: List[str] = []

class Profile(BaseModel):
    name: str
    email: str
    location: str
    linkedin: Optional[str]
    github: Optional[str]
    summary: str
    skills: List[str]
    experience: List[Dict]
    education: List[Dict]
    projects: List[Dict] = []

class Label(BaseModel):
    job_id: str
    relevant: int  # 0/1
    reason: Optional[str] = None