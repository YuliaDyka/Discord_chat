from app import MODEL_TABLENAME, db
from .abstract_model import AbstractModel

class UserHasChat(AbstractModel):
    __tablename__ = MODEL_TABLENAME.get('UserHasChat')

    user_pk = db.Column(db.Integer, db.ForeignKey(MODEL_TABLENAME.get('User') + '.pk'), primary_key=True, nullable=False)
    chat_pk = db.Column(db.Integer, db.ForeignKey(MODEL_TABLENAME.get('Chat') + '.pk'), primary_key=True, nullable=False)
