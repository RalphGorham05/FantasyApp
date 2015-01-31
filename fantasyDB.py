import peewee
from peewee import *

db = MySQLDatabase('fantasyApp', user='root', passwd='')


class BaseModel(Model):
    class Meta():
        database = db

class Team(BaseModel):
    abbr = CharField()
    name = CharField()
    rank = IntegerField()
    pace = IntegerField()
    assists = IntegerField()
    rebs = IntegerField()
    offensiveE = IntegerField()
    defensiveE = IntegerField()




#Player Table
class Player(Model):
    pid = PrimaryKeyField()
    name = CharField()
    position = CharField()

class Meta:
    database = db


Team.create_table()
