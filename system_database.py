import mysql.connector
from mysql.connector import Error
from getpass import getpass
import os

# getpass(prompt='Enter your DB password: '

class StoreDatabase:

    def __init__(self, host = 'localhost', database = "edge_computers"):
        self.host = host
        self.user = os.getenv('MYSQL_USER')
        self.password = os.getenv('MYSQL_PASSWORD')
        self.database = database
    
        try:
            self.__conn = mysql.connector.connect(host = self.host, user = self.user, password = self.password, database = self.database)
            self.__cursor = self.__conn.cursor()
        except Error as e:
            print('An exception occured >>>>> ', e)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()
    
    @property
    def connection(self):
        return self.__conn

    @property
    def cursor(self):
        return self.__cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()
    
    def execute(self, sql_query, params=None):
        try:
            self.cursor.execute(sql_query, params)
        except Error as e:
            print('An error occured while executing >>> ', e)

    def fetchall(self):
        return self.cursor.fetchall()

    def query(self, sql_query, params=None):
        self.cursor.execute(sql_query, params)
        return self.fetchall()


