import os
from flask import Flask

from app.helpers.helper import create_user, list_users

users_file = os.getenv('USERS_FILE')

app = Flask(__name__)

@app.get('/')
def homeRoute():
    return 'Welcome! Let\'s register some users.'

@app.get('/user')
def get_users():
    return list_users()

@app.post('/user')
def register_user():
    return create_user()