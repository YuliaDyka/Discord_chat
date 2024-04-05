from app import MODEL_TABLENAME, db
from .abstract_model import AbstractModel


class Message(AbstractModel):
    __tablename__ = MODEL_TABLENAME.get('Message')

    pk = db.Column(db.Integer, primary_key=True, nullable=False)
    text: str = db.Column(db.Text)
    user_pk = db.Column(db.Integer, db.ForeignKey(MODEL_TABLENAME.get('User') + '.pk'),
                           nullable=False)
    chat_pk = db.Column(db.Integer, db.ForeignKey(MODEL_TABLENAME.get('Chat') + '.pk'))
