from pydantic import BaseModel

class StudyPreferencesBase(BaseModel):
    usuario_id: int
    preferencia: str

class StudyPreferencesCreate(StudyPreferencesBase):
    pass

class StudyPreferencesUpdate(StudyPreferencesBase):
    pass

class StudyPreferences(StudyPreferencesBase):
    id: int

    class Config:
        orm_mode = True