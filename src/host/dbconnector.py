import mysql.connector
from ..catchurl_ext.colorcmd import *

class DBConnector():
    
    def __init__(self):
       self._conn

    def connect(self, host, db, user, password):
        setcol_info()
        print(f"[Connecting to database \"{db}\" as \"{user}\" ]")
        try:
            self._conn = mysql.connector.connect(host=host,database=db,user=user,password=password)
        except Exception as e:
            setcol_error()
            print("  CONNECT DB ERROR: ", e)
        finally:
            if self._conn.is_connected():
                setcol_success()
                print("  Successfully connected")