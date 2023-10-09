from ..in_common import AppRunner
from ..catchurl_ext.colorcmd import *

class HostRunner(AppRunner):

    def run(self):
        super().run()

    def display_menu(self):
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

