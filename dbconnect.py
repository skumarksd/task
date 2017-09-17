__author__ = 'Sucheth'

import MySQLdb
import sys

class DBConnector:
    def __init__(self, username='root', password='skumarksd1234', db='data_engg_task', host='localhost', port=8082, use_unicode=False, staging=False, pool=None):
        self.pool = pool
        self._username = username
        self._password = password
        self._db = db
        self._host = host
        self._port = port
        self.use_unicode = use_unicode
        self._dbh = self.connect()
        self._cursor = self.getCursor()

    def connect(self):
        if self.pool:
            return MySQLdb.connect(self._host, self._username, self._password, self._db, charset='utf8', use_unicode=self.use_unicode)
        else:
            return MySQLdb.connect(self._host, self._username, self._password, self._db, charset='utf8', use_unicode=self.use_unicode)

    def dbHandle(self):
        return self._dbh

    def getCursor(self):

        return self._dbh.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def executeQuery(self, query=''):
        try:
            if not self._dbh:
                self.connect()
            return self._cursor.execute(query)
        except (AttributeError, MySQLdb.OperationalError):
            print "MySQL server gone away reconnecting from dbi instance"
            self.connect()
            return self._cursor.execute(query)

    def getInsertId(self):
        if not self._dbh:
            self.connect()
        return self._cursor.lastrowid

    def executeParameterisedQuery(self, query='', vals=[]):
        try:
            return self._cursor.execute(query, vals)
        except (AttributeError, MySQLdb.OperationalError):
            print "MySQL server gone away reconnecting from dbi instance"
            self.connect()
            return self._cursor.execute(query, vals)

    def fetchRows(self):
        return self._cursor.fetchone()

    def fetchRowsAll(self):
        #self.connect()
        return self._cursor.fetchall()

    def commit(self):
        self._dbh.commit()

    def checkConnection(self):
        return self._dbh.thread_id()

    def escapeString(self, parameter):
        return self._cursor.escape_string(parameter)

    def close_connection(self):
        self._dbh.close()

    def close_cursor(self):
        self._cursor.close()
