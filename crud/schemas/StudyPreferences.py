from pydantic import BaseModel
from typing import List

class StudyPreferencesSchema(BaseModel):
    id: int
    name: str
    description: str
    courses: List[int]
    grade_id: int

    class Config:
        from_attributes = True