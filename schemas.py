from typing import List, Optional
from pydantic import BaseModel, EmailStr


class Education(BaseModel):
    degree: str
    institution: str
    year: Optional[str]


class Experience(BaseModel):
    company: str
    title: str
    duration: Optional[str]
    description: Optional[str]


class Project(BaseModel):
    title: str
    description: Optional[str]


class Certification(BaseModel):
    name: str
    issuer: Optional[str]


class ResumeData(BaseModel):
    name: str
    email: EmailStr
    phone: str
    summary: Optional[str]
    education: List[Education]
    experience: List[Experience]
    skills: List[str]
    projects: List[Project]
    certifications: List[Certification]
