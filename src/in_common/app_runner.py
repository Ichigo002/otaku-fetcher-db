from ..catchurl_ext import *
from ..utils import *
from .dbconnector import *
import xml.etree.ElementTree as ET
import os

class AppRunner():

    def __init__(self, absolute_path="src/host", config_path = "data/config.xml"):
        self._xml_root = None
        self.abs_path = absolute_path
        self._cnf_xml_path = self.normalize_path(config_path)

        self.db = DBConnector()

    def run(self):
        self.load_config()
        self.connect_db()

        sure_exit = False
        while not sure_exit:
            self.display_menu()
            v = fetch_any_usr_input("Choose option")
            os.system("cls")

            match v:
                case "0":
                    sure_exit = True
                case _:
                    setcol_error()
                    print(f"Invalid value: \"{v}\"")
                    
        os.system("cls")
        setcol_summary()
        print("Logged out from database.\nGood Night & Good Luck\n")

    def connect_db(self):
        _pswor = get_usr_password()
        rv = self.db.connect(
            host=self.get_xml_value("./connection/hostname"),
            user=self.get_xml_value("./connection/username"),
            db=self.get_xml_value("./connection/db_name"),
            password=_pswor
        )

        if not rv:
            critical_exit()

    def display_menu(self):
        pass

    def load_config(self): 
        setcol_info() 
        print(f"[Loading XML file \"{self._cnf_xml_path}\"]") 
        
        if not os.path.exists(self._cnf_xml_path): 
            setcol_error() 
            print(f"  LOAD XML ERROR: Couldn't load \"config.xml\" file at \"{self._cnf_xml_path}\"")
            critical_exit()

        tree = ET.parse(self._cnf_xml_path)
        self._xml_root = tree.getroot()

    def normalize_path(self, path):
        return self.abs_path + "/" + path

    def get_xml_value(self, xml_path):
        return self._xml_root.findall(xml_path)[0].text