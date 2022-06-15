from peewee import *
from datetime import *

db = MySQLDatabase(database='ex_13_db', user='root', password='TdQ2spCU/', host='127.0.0.1', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField(max_length=20, unique=True)
    age = BigAutoField
    gender = CharField(max_length=20)
    nationality = CharField(max_length=20)


class Posts(BaseModel):
    id = PrimaryKeyField()
    user_id = ForeignKeyField(User, on_delete='set null', null=True)
    title = CharField(max_length=200)
    description = CharField(max_length=200)
    created = DateTimeField(null=False, default=datetime.now())


class Comments(BaseModel):
    id = PrimaryKeyField()
    text = CharField(max_length=200)
    user_id = ForeignKeyField(User, on_delete='set null', null=True)
    post_id = ForeignKeyField(Posts, on_delete='set null', null=True)


class Likes(BaseModel):
    id = PrimaryKeyField()
    user_id = ForeignKeyField(User, on_delete='set null', null=True)
    post_id = ForeignKeyField(Posts, on_delete='set null', null=True)


User.create_table()
Posts.create_table()
Comments.create_table()
Likes.create_table()

user1 = User(
    name='Don', age=18, gender='M', nationality='USA'
)
user1.save()
