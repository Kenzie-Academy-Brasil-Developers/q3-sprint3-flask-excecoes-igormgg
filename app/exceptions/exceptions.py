from flask import request

class WrongFieldsError(Exception):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.code = 400
        self.description = {'wrong fields': [{'nome': str(type(request.json['nome']))[8:-2]}, {'email': str(type(request.json['email']))[8:-2]}]}

class EmailExistsError(Exception):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.code = 409
        self.description = {'error': 'User already exists.'}