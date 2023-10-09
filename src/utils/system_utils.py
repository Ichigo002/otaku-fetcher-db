from ..catchurl_ext.colorcmd import setcol_clear
import os
from keyboard import on_press, wait

def critical_exit():
    setcol_clear()
    print('\nCritical exit.')
    sys_pause()
    os._exit(-1)

def sys_pause(text_info="Press any key to continue . . ."):
     setcol_clear()
     print(text_info, end="")
     os.system("pause")
     # TODO IT CUZ IT ISN'T FINISHED