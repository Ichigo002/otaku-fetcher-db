from ..catchurl_ext.colorcmd import *
from .client_runner import *
from ..utils import sys_pause


def main():
    app = ClientRunner("data", "config.xml")
    app.run()

if __name__ == "__main__":
    init()
    main()
    sys_pause("Press any key to close terminal . . .")