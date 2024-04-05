import datetime

from flask_restful import Api
from sqlalchemy_utils import database_exists, create_database

from app import app, db, HOST, PORT
from models import *  # DO NOT TOUCH! DB TABLES WILL NOT BE CREATED WITHOUT THIS LINE
from controllers import *


def register_routes(app):
    api = Api(app)

    api.add_resource(UserController, '/user')
    api.add_resource(ChatController, '/chat')
    api.add_resource(MessageController, '/message')
    api.add_resource(UserHasChatController, '/user_has_chat')
    api.add_resource(CSVGeneratorController, '/csv')


def main():
    register_routes(app)
    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        create_database(app.config['SQLALCHEMY_DATABASE_URI'])
    db.create_all()

    app.run(host=HOST, port=HOST, debug=True)


if __name__ == '__main__':
    main()
