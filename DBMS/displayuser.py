# display all user ---------------------------------------------------------------------------------
def display_users():
    try:
        field_oject =open("allusers.txt","r")
    except Exception as e :
        print(e)
    else:
        users = field_oject.readlines()
        print("- "*26)
        print("fname:lname:email-address:password1:password2:phone")
        print("- "*26)
        for user in users:
            print(user.strip('\n'))
        return users
