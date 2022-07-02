from os import close;
from loginuser import login;
from informationuser import regiser

def mainmnu():
    print("enter your choice to login ' l ' to add user ' r '  to close 'c' ")
    try:
        choice = input('enter your choice >> ').lower()
        if choice == "r":
            regiser()
        elif choice == "l":
            login()
        elif choice == "c": 
            close()
        else:
            mainmnu()
    except Exception:
        print("Have a safe road")
 
        


mainmnu()