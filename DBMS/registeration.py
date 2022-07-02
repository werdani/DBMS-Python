from os import close
from displayuser import display_users
from deleteuser import delete_user
from updateuser import update_user
from displaymeu import disply_menu


# dispalay loggin menu.------------------------------------------------------------------------------------- 
def display():
    print('to display "d" to edit "e" to delete "x"  to close "c" ')
    print("to connecte to project 'cp' ")
    try:
        choices = input('enter your choice =>>  ').lower()
        if choices == "d":
            display_users()
        elif choices == "e":
            update_user()
        elif choices == "x":
            delete_user()
        elif choices == "cp":
            disply_menu()
        elif choices == "c":
            close()
        else:
            display()
    except Exception:
        print('Have a safe road')




