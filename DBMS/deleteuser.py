from displayuser import display_users
#to delete users .------------------------------------------------------------------------------
def delete_user():
    allusers = display_users()
    user_delete = input("enter user email to delete =>> ")
    for user in allusers:
        user_info = user.strip("\n")
        user_info = user_info.split(":")
        if user_info[2] == user_delete:
            print("email found")
            allusers.remove(user)
            break
    else:
        return delete_user()
    wirteinuser = open("allusers.txt","w")
    wirteinuser.writelines(allusers)
    wirteinuser.close()