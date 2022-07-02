from os import close
from displaypro import display_projects
from createproject import create_project
from updateproject import update_project
from deleteproject import delete_project

#display menu for projects .---------------------------------------------------------------------------
def disply_menu():
    print("to display all project 'bp' to create 'cp' to edit 'ep' to delete 'd' to close 'c'")
    try:
        choices = input('enter your choice for your project =>>  ').lower()
        if choices == "cp":
            create_project()
        elif choices == "dp":
            display_projects()
        elif choices == "ep":
            update_project()
        elif choices == "d":
            delete_project()
        elif choices == "c":
            close()
        else:
            disply_menu()
    except Exception:
        print('Have a safe road')