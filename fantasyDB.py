import peewee
from peewee import *

db = MySQLDatabase('fantasyApp', user='root', passwd='')


class BaseModel(Model):
    class Meta():
        database = db

class Teams(BaseModel):
    team = CharField()
    city = CharField()
    abbr = CharField()





#Player Table
class Player(Model):
    pid = PrimaryKeyField()
    name = CharField()
    position = CharField()

class Meta:
    database = db


#Stats Table

class Meta:
    database = db

class Stats(Model):
    team = CharField()


r = 5

#Teams.create_table()

