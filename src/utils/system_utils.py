from ..catchurl_ext.colorcmd import setcol_clear
import os

def critical_exit():
    setcol_clear()
    print('\nCritical exit.')
    os.system("pause")
    os._exit(-1)