import os
from json import dump, load
from flask import request

from app.exceptions.exceptions import EmailExistsError, WrongFieldsError

users_file = os.getenv('USERS_FILE')

def list_users():
    if 'database' not in os.listdir('app') or users_file not in os.listdir('app/database') or os.path.getsize(f'app/database/{users_file}') == 0:
        os.system(f"cd app && mkdir database")

        with open(f'app/database/{users_file}', 'w') as f:
            default_user_list = { "data": [] }
            dump(default_user_list, f, indent=4)
            
    with open(f'app/database/{users_file}', 'r') as r:
        return load(r), 200

def create_user():
    if 'database' not in os.listdir('app') or users_file not in os.listdir('app/database'):
        os.system(f"cd app && mkdir database")

        with open(f'app/database/{users_file}', 'w') as f:
            default_user_list = { "data": [] }
            dump(default_user_list, f, indent=4)

    try:
        if type(request.json['nome']) != str or type(request.json['email']) != str:
            raise WrongFieldsError()

        user_to_be_created = {}
        user_to_be_created['nome'] = request.json['nome'].title()
        user_to_be_created['email'] = request.json['email'].lower()
        with open(f'app/database/{users_file}', 'r') as r:
            user_to_be_created['id'] = len(load(r)['data']) + 1
        
        users_dict = list_users()[0]

        for user in users_dict['data']:
            if user_to_be_created['email'] == user['email']:
                raise EmailExistsError()
        
        output = {'data': user_to_be_created}

        users_dict['data'].append(user_to_be_created)

        with open(f'app/database/{users_file}', 'w') as w:
            dump(users_dict, w, indent=4)

        return output, 201
    
    except EmailExistsError as err:
        return err.description, err.code
    
    except WrongFieldsError as err:
        return err.description, err.code