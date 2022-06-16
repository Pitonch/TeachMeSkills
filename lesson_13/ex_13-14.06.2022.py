from peewee import *
from datetime import *

db = MySQLDatabase(database='ex_13_db', user='root', password='TdQ2spCU/', host='127.0.0.1', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField(max_length=20, unique=True)
    age = IntegerField(constraints=[Check('age>0 and age<120')])
    gender = CharField(max_length=20)
    nationality = CharField(max_length=20)


class Posts(BaseModel):
    id = PrimaryKeyField()
    user_id = ForeignKeyField(User, on_delete='set null', null=True)
    title = CharField(max_length=200)
    description = CharField(max_length=200)
    created = DateTimeField(null=False, default=datetime.now())
    likes = ManyToManyField(User, on_delete='cascade')


Likes = Posts.likes.get_through_model()


class Comments(BaseModel):
    id = PrimaryKeyField()
    text = TextField()
    user_id = ForeignKeyField(User, on_delete='set null', null=True)
    post_id = ForeignKeyField(Posts, on_delete='set null', null=True)


# class Likes(BaseModel):
#     id = PrimaryKeyField()
#     user_id = ForeignKeyField(User, on_delete='set null', null=True)
#     post_id = ForeignKeyField(Posts, on_delete='set null', null=True)

# Likes.drop_table()
# Comments.drop_table()
# Posts.drop_table()
# User.drop_table()


User.create_table()
Posts.create_table()
Comments.create_table()
Likes.create_table()

# user1 = User(name='Don', age=18, gender='M', nationality='USA')
# user1.save()
#
# User.create(name='Ann', age=15, gender='F', nationality='USA')
# User.create(name='X', age=100, gender='F', nationality='USA')
# #
# # users = User.select().execute()
# #
# # for x in users:
# #     print(x.name)
#
# data = [{'name': '1', 'age':13, 'gender':'f', 'nationality':'rus'},
#         {'name':'vfv', 'age':11, 'gender':'m', 'nationality':'rus'},
#         {'name':'sadf', 'age':35, 'gender':'m', 'nationality':'bel'},
#         {'name':'fdsh', 'age':19, 'gender':'f', 'nationality':'bel'}]
#
# # User.insert_many(data, fields=[User.name, User.age, User.gender, User.nationality]).execute()
#
# user1 = User(**data[0]).save()
# Posts.create(
#     user_id=user1,
#     title="хаха",
#     description='dhsluadbsl;'
# )


