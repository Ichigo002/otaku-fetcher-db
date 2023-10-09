from ..in_common import AppRunner
from ..catchurl_ext.colorcmd import *
from os import system

class HostRunner(AppRunner):

    def display_menu(self):
        system("cls")
        setcol_decorative()
        print("\n --===-- ")
        setcol_summary()
        print(  f"| Logged into {self.get_xml_value('./connection/db_name')} ",
              f"\n| as {self.get_xml_value('./connection/username')} @",
              f"{self.get_xml_value('./connection/hostname')}")
        setcol_decorative()
        print("--===-- ")
        setcol_info()

        print("0. Log out")
        print("1. Upload URL")
        print("2. Upload from CSV")
        print("3. Reset database")
        print("4. Show database")
        
        setcol_decorative()
        print(" --===--")

    def handle_chose_menu_option(self, chose):
        match(chose):
            case "0":
                return True
            case "1":
                self.chmenu_upload_url()
            case _:
                self.handle_match_unknown_case(chose)

        return False
    
    def chmenu_upload_url(self):
        setcol_decorative()
        print("\n --===--")
        setcol_summary()
        print("| Option: UPLOAD URL")

        system("pause")

