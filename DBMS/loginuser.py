from registeration import display
def login():
    email = input('enter your email =>> ')
    password = input('enter your password =>> ')
    try:
        file_object = open("allusers.txt","r")
    except Exception as e :
        return login()
    else:
        users = file_object.readlines()
        for user in users:
            user_data = user.strip('\n')
            user_info = user_data.split(":")
            if user_info[2] == email and user_info[3] == password:
                print(" *"*12)
                print('| logged in successfuly |')
                print(" *"*12)
                display()
                break
            else:
                print('logged field')
                return login()