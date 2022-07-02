from displaypro import display_projects

#delete project .------------------------------------------------------------------------------------------------------
def delete_project():
    allproject = display_projects()
    owner = input("enter  email for project owner  =>> ")
    price = input("enter  total for project =>> ")
    for project in allproject:
        user_info = project.strip("\n")
        user_info = user_info.split(":")
        if user_info[0] == owner and user_info[3] == price:
            print("email found")
            allproject.remove(project)
            print("deleted successfuly")
            break
    else:
        print("check your input")
        return delete_project()
    wirteinuser = open("projects.txt","w")
    wirteinuser.writelines(allproject)
    wirteinuser.close()
