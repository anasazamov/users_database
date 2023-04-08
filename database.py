from tinydb import TinyDB, Query
from tinydb.operations import delete

db = TinyDB('db.json', indent=4, separators=(',', ': '))
users_table = db.table('users')


User = Query()

def get_by_field(field: str, value: str):
    '''Returns a user by field'''
    return users_table.search(User[field].search(value))


def get_user_by_id(user_id):
    '''Returns a user by id'''
    return users_table.get(doc_id=user_id)

def get_user_by_email(email):
    '''Returns a user by email'''
    return users_table.search(User.email==email)


def get_user_by_first_name(first_name):
    '''Returns a user by first name'''
    return users_table.search(User.first_name==first_name)

def get_user_by_last_name(last_name):
    '''Returns a user by last name'''
    return users_table.search(User.last_name==last_name)

def get_user_by_country(country):
    '''Returns a user by country'''
    return users_table.search(User.country==country)

def get_users_full_name(user):
    '''Returns a user's full name'''
    json= users_table.get(doc_id=user)
    return f'{json["first_name"]} {json["last_name"]}'


def update_user(user_id, field, value):
    '''Updates a user's field'''
    users_table.update({field:value},doc_ids=user_id)
def delete_user(user_id):
    '''Deletes a user'''
    users_table.remove(doc_ids=[user_id])

def add_user(user: dict):
    '''Adds a user to the database'''
    users_table.insert(user)
print(update_user("mbrodest1@yale.edu"))