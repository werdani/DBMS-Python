def display_projects():
    try:
        field_oject =open("projects.txt","r")
    except Exception as e :
        print(e)
    else:
        porjec = field_oject.readlines()
        print("- "*26)
        print("pname:ptitle:total taregt:start date : end date")
        print("- "*26)
        for pro in porjec:
            print(pro.strip('\n'))
        return porjec
