from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional, Dict

from cv_generator import Activity, Contact, Education, Experience, Header, Language, Project, Skill, Summary
# The import works, but the editor might not recognize it due to relative import issues.
# Ensure that the package is properly installed or marked as a source root in your editor.
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
    activities: Optional[List[Activity]]
    contact: Optional[Contact]
    education: Optional[List[Education]]
    experiences: Optional[List[Experience]]
    header: Optional[List[Header]]
    languages: Optional[List[Language]]
    pic: Optional[str]
    projects: Optional[List[Project]] = []
    skills: Optional[List[Skill]]
    summary: Optional[List[Summary]]

class Label(BaseModel):
    job_id: str
    relevant: int  # 0/1
    reason: Optional[str] = None