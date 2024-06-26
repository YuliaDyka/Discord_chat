from os import getenv
from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from utils import CustomJSONEncoder

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DB_CONN_STR')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json_encoder = CustomJSONEncoder

db = SQLAlchemy(app)

HOST = getenv('FLASK_HOST')
PORT = getenv('FLASK_PORT')


MODEL_TABLENAME = {
    'User': 'users',
    'Chat': 'chats',
    'Message': 'messages', 
    'UserHasChat': 'user_has_chat'
}
