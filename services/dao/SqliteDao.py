import os
import sqlite3
from abc import ABCMeta, abstractmethod
from sqlite3 import Cursor, Connection

from common.ConfigUtils import getConfig, SQLITE_FILE

'''
   @Author Jiage
   @Date 2021-09-08
   @Description connect database,parent class,provide basically access database
    the methods, like query,execute...
'''
class SqliteDao(metaclass=ABCMeta):

    # init connect the database
    def __init__(self):
        self.config = getConfig()
        self.filePath = self.config.get(SQLITE_FILE)
        self._conn = sqlite3.connect(self.filePath, check_same_thread=False)
        # init necessary tables
        self.__initTables()

    # query data
    @abstractmethod
    def query(self, value) -> list:
        pass

    # create or modify data
    @abstractmethod
    def updateOrInsert(self, value) -> int:
        pass

    # connect database
    @property
    def conn(self) -> Connection:
        if self._conn is None:
            print("connect is null create a new instance")
            self._conn = sqlite3.connect(self.filePath)
        return self._conn

    # close database
    def close(self):
        if self._conn is not None:
            print("close current database connect")
            self._conn.close()
            self._conn = None

    # fetch all data
    def fetch(self, sql) -> list:
        c = self.conn.cursor()
        rs = c.execute(sql).fetchall()
        c.close()
        return rs

    # get one data, like get count or state data
    def fetchOneInt(self, sql) -> int:
        c = self.conn.cursor()
        rs = c.execute(sql).fetchone()
        c.close()
        return rs[0]

    # execute sql script like create,insert and update
    def execute(self, sql) -> int:
        c = self.conn.cursor()
        c.execute(sql)
        rs = self.conn.total_changes
        self._conn.commit()
        return rs

    # init database
    def __initTables(self):
        c = self.conn.cursor()
        count = c.execute("SELECT COUNT(*) as count FROM sqlite_master where type='table' and name='auto_scale_setting'").fetchone()[0]
        if count == 1:
            c.close()
            return
        # starting init tables
        c.executescript('''
         CREATE TABLE auto_scale_setting(
            mini_size    int NOT NULL,
            max_size     int NOT NULL,
            mem_exc      int    
        );
        ''')
        print("init tables successful.")
        self._conn.commit()
        c.close()