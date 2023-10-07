from ..catchurl_ext.colorcmd import *
import pwinput

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

def get_usr_password():
     setcol_question()
     print("Enter user's password\n:>", end="")
     setcol_user_input()
     return pwinput.pwinput(" ", mask="*")