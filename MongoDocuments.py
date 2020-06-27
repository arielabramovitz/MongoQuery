from mongoengine import *
from mongoengine.context_managers import *
import datetime
import binascii

connect(alias='UsersInfo', db='UsersInfo')
connect(alias='ClientsInfo' ,db='ClientsInfo')


class Users(Document):
    username = StringField(required=True, unique=True, max_length=30)
    password = BinaryField(required=True)
    email = EmailField(required=True)
    registration_date = datetime.datetime.now().strftime("%d/%m/%Y at %H:%M")
    bio = StringField(max_length=100)
    admin = BooleanField(default=False)

    meta = {'db_alias': 'UsersInfo', 'collection': 'Users'}

class Client(Document):
    username = StringField(required=True, unique=True, max_length=30)
    password = BinaryField(required=True)
    email = EmailField(required=True)
    registration_date = datetime.datetime.now().strftime("%d/%m/%Y at %H:%M")
    bio = StringField(max_length=100)

    meta = {'db_alias': 'ClientsInfo', 'collection': 'Clients'}

with switch_db(Client, 'ClientsInfo') as Client:
    with switch_collection(Client, 'Clients') as Client:
        user = Client(username='ariel2', password=binascii.a2b_base64('20051996'), email='ariel2@gmail.com').save()

