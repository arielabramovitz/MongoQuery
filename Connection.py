from mongoengine import *
import MongoDocuments

class Connection:

    current_active = None

    def __init__(self, **kwargs):
        self.host = 'localhost'
        self.port = 27017
        if len(kwargs) == 0:
            Connection.current_active = connect(host=self.host, port=self.port)
        else:
            connect()
        if "alias" and "db" in kwargs.keys():
            Connection.current_active = connect(host=self.host, port=self.port, db=kwargs['db'], alias=kwargs['alias'])

    def get_dbs(self):
        return Connection.current_active.list_database_names()[:-3]

    def get_collections_of_db(self, db):
        return Connection.current_active[db].list_collection_names()

    def get_all_collections(self):
        collections = dict()
        for db in self.get_dbs():
            collections[db] = Connection.current_active.list_collection_names()

        return collections

    def get_objects(self, db, collection):
        objects = dict()
        if db == 'UsersInfo' and collection == 'Users':
            objects = [k.dict() for k in MongoDocuments.Users.objects]
        elif db == 'ClientsInfo' and collection == 'Clients':
            objects = [j.dict() for j in MongoDocuments.Clients.objects]
        else:
            return -1
        return objects

    @classmethod
    def get_document_fields(cls, doc):
        return doc.fields()

connection1 = Connection()
print('DB List:')
print(connection1.get_dbs())
print("Collections in 'UsersInfo':")
print(connection1.get_collections_of_db('UsersInfo'))
print("Collections in 'ClientsInfo':")
print(connection1.get_collections_of_db('ClientsInfo'))
print("Objects in 'Users':")
connection1 = Connection(db='UsersInfo', alias='UsersInfo')
print(connection1.get_objects('UsersInfo','Users')[0])
print("Objects in 'Clients':")
connection1 = Connection(db='ClientsInfo', alias='ClientsInfo')
print(connection1.get_objects('ClientsInfo','Clients')[0])





