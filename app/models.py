from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import app, db
from sqlalchemy.exc import IntegrityError


class Borough(db.Model):
    __tablename__ = 'borough'
    __table_args__ = {'extend_existing': True}
    borough_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, id, name):
        self.borough_id = id
        self.name = name

    def __repr__(self):
        return f"Borough: ('{self.borough_id}', '{self.name}')"

