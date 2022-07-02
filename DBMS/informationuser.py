from mailvalidation import check
from checkphone import checkphone

# user register info .---------------------------------------------------------------------------------------
def information():
    global first_name,last_name,email_add,password1,password2,phone_num
    while True:
        first_name = input("Enter your First name =>> ")
        last_name  = input("Enter your Last name =>> ")
        email_add  = input("Enter your Email =>> ")
        if check(email_add) == False:
            break
        password1  = input("Enter your password =>> ")
        password2  = input("Confirm your password =>> ")
        if password1 != password2:
            print('not the same password,try again......')
            break
        phone_num  = input("Enter your Mobile phone =>> ")
        if checkphone(phone_num) == False: 
            break
        break  
      
#-----------------------------------------------------------------------------------------------------------------

def regiser():
    information()
    print('register successfully')
    try:
        file_object = open("allusers.txt","a")
    except Exception as e :
        return regiser
    else:
        user_info = f'{first_name}:{last_name}:{email_add}:{password1}:{password2}:{phone_num}\n'
        file_object.write(user_info)
        file_object.close
