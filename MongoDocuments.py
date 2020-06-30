from mongoengine import *
import datetime
import binascii

class Users(Document):
    username = StringField(required=True, unique=True, max_length=30)
    password = BinaryField(required=True)
    email = EmailField(required=True)
    registration_date = datetime.datetime.now().strftime("%d/%m/%Y at %H:%M")
    bio = StringField(max_length=100)
    admin = BooleanField(default=False)

    def __str__(self):
        return f'Username: {self.username}, Email: {self.email}'

    @staticmethod
    def fields():
        return [i for i in Users.fields_ordered]

    def dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'registration_date': self.registration_date,
            'bio': self.bio,
            'admin': self.admin
        }

    meta = {'db_alias': 'UsersInfo', 'collection': 'Users'}

class Clients(Document):
    username = StringField(required=True, unique=True, max_length=30)
    password = BinaryField(required=True)
    email = EmailField(required=True)
    registration_date = datetime.datetime.now().strftime("%d/%m/%Y at %H:%M")
    bio = StringField(max_length=100)

    meta = {'db_alias': 'ClientsInfo', 'collection': 'Clients'}

# with switch_db(Client, 'ClientsInfo') as Client:
#     with switch_collection(Client, 'Clients') as Client:
#         user = Client(username='ariel2', password=binascii.a2b_base64('20051996'), email='ariel2@gmail.com').save()
# connection1 = connect(alias='ClientsInfo', db='ClientsInfo', host='localhost', port=27017)
# connection2 = connect(alias='UsersInfo', db='UsersInfo', host='localhost', port=27017)
# user = Users(username='ariel4', password=binascii.a2b_base64('20051996'), email='ariel4@gmail.com').save()

