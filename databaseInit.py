import pymysql

class DB:
    def __init__(self):
        self.connection, self.cursor = self.init()
        self.buildDB(self.connection, self.cursor)

    def init(self):
        self.connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234root')
        self.cursor = self.connection.cursor()
        return self.connection, self.cursor

    def buildDB(self, connection, cursor):
        query = "CREATE DATABASE IF NOT EXISTS Timer;"
        cursor.execute(query)
        connection.commit()
        query = "USE Timer;"
        cursor.execute(query)
        connection.commit()
        query = "CREATE TABLE IF NOT EXISTS Records(\
                    date DATETIME,\
                    tag VARCHAR(20),\
                    duration TIME,\
                    associatedGoal INT\
                    )"
        cursor.execute(query)
        connection.commit()

    def exec(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def getConnectionInfo(self):
        return self.connection, self.cursor