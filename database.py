from tinydb import TinyDB, Query

db = TinyDB('db.json', indent=4, separators=(',', ': '))
users = db.table('users')


def get_users() -> list:
    '''Returns a list of users from the database.'''
    pass

def get_user_by_id(id: int) -> dict:
    '''Returns a user by their ID.'''
    pass

def get_user_by_full_name(first_name: str, last_name: str) -> dict:
    '''Returns a user by their full name.'''
    pass