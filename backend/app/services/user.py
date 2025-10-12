from sqlalchemy.orm import Session
from app.orm.user import User

def _get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.user_id == user_id).first()

def _create_user(db: Session, user_data: dict):
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def _user_in_db(db: Session, user_id: str):
    return db.query(User).filter(User.user_id == user_id).first() is not None

def _update_user(db: Session, user_id: str, update_data: dict):
    user = _get_user_by_id(db, user_id)
    if not user:
        return None
    for key, value in update_data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def _get_internal_user_id(db: Session, user_id: str):
    user = _get_user_by_id(db, user_id)
    if user:
        return user.id
    return None

def _get_auth0_id(db: Session, internal_id: int):
    user = db.query(User).filter(User.id == internal_id).first()
    if user:
        return user.user_id
    return None