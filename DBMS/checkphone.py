import re

# to check phone number ---------------------------------------------------------------------------------
def checkphone(phone):
    if re.fullmatch("^01[0125][0-9]{8}$",phone):
        print("valid phone")
    else:
        print ("not valid phone try agan....")

