from PyQt5.QtWidgets import QMessageBox
# from gui import *
from mongoengine import *
import mongoengine

active = None


def connect_to_mongo():
    global active
    active = connect(host='localhost', port=27017)
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
    items = dict()


connect_to_mongo()

cursor = active['UsersInfo']['Users'].find
gen = (i for i in cursor)
print(next(gen))
