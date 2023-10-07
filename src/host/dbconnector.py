import mysql.connector
from ..catchurl_ext.colorcmd import *

class DBConnector():
    
    def __init__(self):
       self._conn = None

    def connect(self, host, db, user, password):
        setcol_info()
        print(f"[Connecting to database \"{db}\" as \"{user}\"]")
        try:
            self._conn = mysql.connector.connect(host=host,database=db,user=user,password=password)
        except mysql.connector.errors.DatabaseError as e:
            msg = "" 
            match e.errno:
                case 1045:
                    msg = "Access denied for user. Probably incorrect password, user or server blocks your ip."
                case _:
                    msg = e
            setcol_error()
            print("  CONNECT DATABASE ERROR: ", msg)
            return False
        except Exception as e:
            setcol_error()
            print("  CONNECT DATABASE ERROR:", e)
            return False
        
        if self._conn.is_connected():
            setcol_success()
            print("  Successfully connected")
            return True
        return False