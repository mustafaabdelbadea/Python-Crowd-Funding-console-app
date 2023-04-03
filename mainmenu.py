from users import login, register


def mainMenu():
    choice = int(input("Please enter 1- for login\n2- for register \n"))
    match choice:
        case 1:
            value = login()
            if value:
                projectsMenu(value)
        case 2:
            register()
        case default:
            print("Enter a valid choice ")
            mainMenu()


def projectsMenu(userId):
    choice = int(input("Please enter 1- for create new project\n2- for view all projects \n3- Edit your project\n4- Delete project\n5- Search for specific project"))
    match choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5: 
            pass
        case default:
            print("Enter a valid choice")
            projectsMenu(userId)

mainMenu()