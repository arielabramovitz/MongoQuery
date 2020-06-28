from MongoDocuments import *
from mongoengine import *


active = None


def connect_to_mongo():
    global active
    active = [connect(host='localhost', port=27017, db='UsersInfo', alias='UsersInfo'),
              connect(host='localhost', port=27017, db='ClientsInfo', alias='ClientsInfo')]
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
        items_as_dicts = [i.dict() for i in Users.objects]
    elif db == 'ClientsInfo' and collection == 'Clients':
        items_as_dicts = [i.dict() for i in Clients.objects]
    return items_as_dicts

connect_to_mongo()

objects = Users.objects
print(Users.fields())
print(get_items('UsersInfo','Users'))
