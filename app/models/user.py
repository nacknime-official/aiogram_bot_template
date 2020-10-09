from app.models.db import TimedBaseModel, db


class User(TimedBaseModel):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
