import pymysql

class DB:
    def __init__(self):
        self.connection, self.cursor = self.init()
        self.buildDB(self.connection, self.cursor)

    def init():
        connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234root')
        cursor = connection.cursor()
        return connection, cursor

    def buildDB(connection, cursor):
        query = "CREATE DATABASE TIMER"
        cursor.execute(query)
        connection.commit()
        query = "CREATE TABLE Records(\
                    date DATETIME\
                    tag VARCHAR(20)\
                    duration TIMESTAMP\
                    associatedGoal SET('Y', 'N')\
                    )"
        cursor.execute(query)
        connection.commit()

    def exec(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def getConnectionInfo(self):
        return self.connection, self.cursor