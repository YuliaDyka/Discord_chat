from app import MODEL_TABLENAME, db
from .abstract_model import AbstractModel


class Chat(AbstractModel):
    __tablename__ = MODEL_TABLENAME.get('Chat')

    pk = db.Column(db.Integer, primary_key=True, nullable=False)
    admin_pk: int = db.Column(db.Integer, db.ForeignKey(MODEL_TABLENAME.get('User') + '.pk'),
                           nullable=False)
    name: str = db.Column(db.String(45))

    messages = db.relationship('Message')

    users = db.relationship('User', secondary=MODEL_TABLENAME.get("UserHasChat"))

    