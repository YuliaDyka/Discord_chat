
from app import MODEL_TABLENAME, db
from .abstract_model import AbstractModel

class User(AbstractModel):
    __tablename__ = MODEL_TABLENAME.get('User')

    pk = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(45), nullable=False)
    email: str = db.Column(db.String(45), nullable=False, unique=True)
    password: str = db.Column(db.String(45), nullable=False)

    messages = db.relationship('Message')
