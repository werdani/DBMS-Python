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
                title = input("enter  title >> ")
                user_info[1] = title
            elif edit_part == "d":
                discription = input("enter your discription >> ")
                user_info[2] = discription
            elif edit_part == "p":
                total = input('enter your total >> ')
                user_info[3] = total
            else :
                return update_project() 
            updateproject = ":".join(user_info)
            updateproject = f"{updateproject}\n" 
            userindex = allproject.index(project)
            allproject[userindex] =updateproject

            break
    else:
        return update_project()
    wirteinuser = open("projects.txt","w")
    wirteinuser.writelines(allproject)
    wirteinuser.close()


    pass



