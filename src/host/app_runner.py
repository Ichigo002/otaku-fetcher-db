from ..catchurl_ext import *
import xml.etree.ElementTree as ET

class AppRunner():

    def __init__(self, absolute_path="src/host", config_path = "data/config.xml"):
        self._xml_root = None
        self.abs_path = absolute_path
        self._cnf_xml_path = self.normalize_path(config_path)

    def run(self):
        self.load_config()
        print(self.get_xml_value("./csv/load_path"))

    def display_menu(self):
        pass

    def load_config(self):
        tree = ET.parse(self._cnf_xml_path)
        self._xml_root = tree.getroot()

    def normalize_path(self, path):
        return self.abs_path + "/" + path

    def get_xml_value(self, xml_path):
        return self._xml_root.findall(xml_path)[0].text