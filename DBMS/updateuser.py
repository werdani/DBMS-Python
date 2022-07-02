from displayuser import display_users

#to update user -----------------------------------------------------------------------------------------------
def update_user():
    allusers = display_users()
    user_edit = input("enter user email to update =>> ")
    for user in allusers:
        user_info = user.strip("\n")
        user_info = user_info.split(":")
        if user_info[2] == user_edit:
            print("email found")
            print('choice a part edit\n>> to fname "fn" to lname "ln" to email "e"\n>>to password "p" to phone "t"')
            edit_part = input('enter your choice >> ').lower()
            if edit_part == "fn":
                fname = input("enter first name >> ")
                user_info[0] = fname
            elif edit_part == "ln":
                lname = input("enter last name >> ")
                user_info[1] = lname
            elif edit_part == "e":
                email = input('enter your email >> ')
                user_info[2] = email
            elif edit_part == "p":
                password1 = input('enter your password >> ')
                password2 = input('confearme your password >> ')
                user_info[3] = password1
                user_info[4] = password2
            elif edit_part == "t":
                phone = input('enter your phone number >> ')
                user_info[5] = phone
            else :
                return update_user() 
            updateduser = ":".join(user_info)
            updateduser = f"{updateduser}\n" 
            userindex = allusers.index(user)
            allusers[userindex] =updateduser

            break
    else:
        return update_user()
    wirteinuser = open("allusers.txt","w")
    wirteinuser.writelines(allusers)
    wirteinuser.close()




