from ..catchurl_ext.colorcmd import *

def fetch_usr_input(display_text):
    input_txt = display_text + " (Y/n)?\n:> "

    setcol_question()
    print(input_txt, end="")
    setcol_user_input()
    output = str(input())
    setcol_clear()
    return check_usr_inputYN(output)

def check_usr_inputYN(input):
    return (input.lower() == "y")