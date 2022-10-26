from helpers.database import db


class Prefeitura():
 
    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<Prefeitura %r>' % self.email
