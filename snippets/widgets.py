#!/usr/bin/env python

from project.server import app, db, bcrypt
from CustomLogging import DBLogHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)
handler = DBLogHandler()
handler.setLevel(logging.WARN)
logger.addHandler(handler)

class CompareWidget(db.Model):
    """User model for use by the two compare widgets"""
    __tablename__ = "compare_widget"

    user_id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    country = db.Column(db.String(255))
    occupation = db.Column(db.String(255))
    salary = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

