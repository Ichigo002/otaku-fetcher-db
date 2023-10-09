from ..catchurl_ext.colorcmd import *
from .host_runner import *
import os


def main():
    app = HostRunner()
    app.run()

if __name__ == "__main__":
    init()
    main()
    setcol_clear()
    os.system("pause")