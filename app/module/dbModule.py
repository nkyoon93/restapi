#when add new module -> for importing

import pymysql

class Database():
    def __init__(self): #DB-connect
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  db='your_dbname',
                                  charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor) #make cursor for interaction with connected DB

    def execute(self, query, arg={}):
        self.cursor.execute(query, arg) #do sql

    def executeOne(self, query, arg={}):
        self.cursor.execute(query, arg)
        row = self.cursor.fetchall() #fetchall -> get sql result
        return row
    def commit():
        self.db.commit()