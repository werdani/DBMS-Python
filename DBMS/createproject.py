def create_project():
    project_email = input("Enter email for project owner =>>")
    project_title = input("Enter your project name =>> ")
    project_details  = input("Enter your details =>> ")
    total_target   = input("Enter your total target =>> ")
    print('added successfully')
    try:
        file_object = open("projects.txt","a")
    except Exception as e :
        return create_project
    else:
        project_info = f'{project_email}:{project_title}:{project_details}:{total_target}\n'
        file_object.write(project_info)
        file_object.close()
