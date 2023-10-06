from ..catchurl_ext.colorcmd import *
from .app_runner import *
import os


def main():
    app = AppRunner()
    app.run()

if __name__ == "__main__":
    init()
    main()
    setcol_clear()
    os.system("pause")