from MongoDocuments import *
from mongoengine import *
import binascii

active = None

# edit function involving variable active to work with a dictionary instead of a single connection

def connect_to_mongo():
    global active
    active = {'UsersInfo': connect(host='localhost', port=27017, db='UsersInfo', alias='UsersInfo'),
              'ClientsInfo': connect(host='localhost', port=27017, db='ClientsInfo', alias='ClientsInfo')}
    return active


def list_databases():
    global active
    return active.list_database_names()[:-3]


def list_collections():
    global active
    collections = dict()
    for d in list_databases():
        collections[d] = active[d].list_collection_names()
    return collections

def get_items(db, collection):
    items_as_dicts = None
    if db == 'UsersInfo' and collection == 'Users':
        items_as_dicts = [k.dict() for k in Users.objects]
    elif db == 'ClientsInfo' and collection == 'Clients':
        items_as_dicts = [j.dict() for j in Clients.objects]
    return items_as_dicts

def pass_encoder(password):
    encoded_pass = binascii.a2b_base64(password)
    return encoded_pass

def password_decoder(password):
    decoded_pass = binascii.b2a_base64(password).decode('utf-8').strip()
    return decoded_pass


connect_to_mongo()

for i in list(get_items('UsersInfo','Users')):
    print(list(i.keys()))
    print()
