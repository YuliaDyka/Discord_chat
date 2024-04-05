from typing import Type

from flask_restful import reqparse
from flask import request, jsonify, make_response

from models.user import User
from models.user_has_chat import UserHasChat
from models import Chat
from .abstract_controller import AbstractController


class ChatController(AbstractController):
    _parser = reqparse.RequestParser()

    @classmethod
    def get_model(cls) -> Type[Chat]:
        return Chat

    @classmethod
    def get_parser(cls) -> reqparse.RequestParser:
        return cls._parser

    @classmethod
    def post(cls):
        data = request.get_json()
       
        new_chat = Chat(**data)
        new_chat._save()
        return jsonify(new_chat)
    
    # @classmethod
    # def get(cls):
    #     data = request.get_json()
    
    
class UserHasChatController(AbstractController):
    _parser = reqparse.RequestParser()
    @classmethod
    def post(cls):
        data = request.get_json()
        if not User.query.filter_by(pk=data['user_pk']).first():
                return make_response("User not found", 400)
        if not Chat.query.filter_by(pk=data['chat_pk']).first():
                return make_response("Chat not found", 400)
        
       
        new_user_has_chat = UserHasChat(**data)
        new_user_has_chat._save()
        return jsonify(new_user_has_chat)

