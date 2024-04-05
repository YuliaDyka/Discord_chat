from typing import Type
from flask_restful import reqparse
from flask import request, jsonify, make_response


from models.user import User
from models.user_has_chat import UserHasChat
from models import Message
from .abstract_controller import AbstractController


class MessageController(AbstractController):
    _parser = reqparse.RequestParser()

    @classmethod
    def get_model(cls) -> Type[Message]:
        return Message

    @classmethod
    def get_parser(cls) -> reqparse.RequestParser:
        return cls._parser
    
    @classmethod
    def post(cls):
        data = request.get_json()
        if not User.query.filter_by(pk=data['user_pk']).first():
                return make_response("User not found", 400)
        # if not Chat.query.filter_by(pk=data['chat_pk']).first():
        #         return make_response("Chat not found", 400)
            
        new_message = Message(**data)
        new_message._save()
        return jsonify(new_message)