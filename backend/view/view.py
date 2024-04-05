from models import User, Message


class View ():
    def create_chat(self, user_id: int, chat_name: str):
        pass
    def add_user_to_chat(self, user_id: int, chat_id: int):
        pass
    def get_chat_users(self, chat_id: int) -> list [User]:
        pass
    def get_chat_messages(self, chat_id: int) -> list [Message]:
        pass
    def add_message_to_chat(self, chat_id: int, user_id: int,) -> list [Message]: 
        pass