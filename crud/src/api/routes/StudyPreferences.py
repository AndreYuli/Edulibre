from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.StudyPreference import StudyPreferencesCreate, StudyPreferences
from src.models.StudyPreference import StudyPreference
from src.api.deps import get_db
from sqlalchemy.exc import IntegrityError
import logging

router = APIRouter()

@router.post("/", response_model=StudyPreferences)
def save_user_preferences(study_preferences: StudyPreferencesCreate, db: Session = Depends(get_db)):
    logging.info(f"Received preferences: {study_preferences}")
    try:
        user_preferences = db.query(StudyPreference).filter(StudyPreference.usuario_id == study_preferences.usuario_id).first()
        if user_preferences:
            user_preferences.preferencia = study_preferences.preferencia
        else:
            user_preferences = StudyPreference(
                usuario_id=study_preferences.usuario_id,
                preferencia=study_preferences.preferencia
            )
        db.add(user_preferences)
        db.commit()
        db.refresh(user_preferences)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=409, detail="Conflict: User preference already exists")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return user_preferences