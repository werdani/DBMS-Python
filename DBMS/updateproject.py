from displaypro import display_projects
# update project---------------------------------------------------------------------------------------------------
def update_project():
    allproject = display_projects()
    user_edit = input("enter user email to update =>> ")
    for project in allproject:
        user_info = project.strip("\n")
        user_info = user_info.split(":")
        if user_info[0] == user_edit:
            print("email found")
            print('choice a part edit\n>> to pname "n" to pdescription "d" to price "p"\n>>to password "p" to phone "t"')
            edit_part = input('enter your choice >> ').lower()
            if edit_part == "n":
                fname = input("enter  title >> ")
                user_info[1] = fname
            elif edit_part == "d":
                lname = input("enter your discription >> ")
                user_info[2] = lname
            elif edit_part == "p":
                email = input('enter your total >> ')
                user_info[2] = email
            else :
                return update_project() 
            updateduser = ":".join(user_info)
            updateduser = f"{updateduser}\n" 
            userindex = allproject.index(project)
            allproject[userindex] =updateduser

            break
    else:
        return update_project()
    wirteinuser = open("projects.txt","w")
    wirteinuser.writelines(allproject)
    wirteinuser.close()


    pass



