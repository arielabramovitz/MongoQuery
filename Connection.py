from mongoengine import *

class Connection:

    current_active = None

    def __init__(self, **kwargs):
        self.host = 'localhost'
        self.port = 27017
        if len(kwargs) == 0:
            connect(host=self.host, port=self.port)
        else:
            connect()
        if "alias" and "db" in kwargs.keys():
            connect(host=self.host, port=self.port, db=kwargs['db'], alias=kwargs['alias'])

    def get_dbs(self):
        return self.list_database_names()[:-3]

    def get_collections(self, db):
        collections = dict()
        for db in self.get_dbs():
            collections[db] = self.list_collection_names()


