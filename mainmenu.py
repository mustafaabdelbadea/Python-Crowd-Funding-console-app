from users import login, register
from projects import createPorject, getAllProjects, searchForProject, deleteProject, editProject

def mainMenu():
    choice = int(input("Please enter\n1- for login\n2- for register \n"))
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
    choice = int(input("Please enter\n1- for create new project\n2- for view all projects \n3- Edit your project\n4- Delete project\n5- Search for specific project "))
    match choice:
        case 1:
            createPorject(userId)
        case 2:
            getAllProjects()
        case 3:
            editProject(userId)
        case 4:
            deleteProject(userId)
        case 5: 
            searchForProject()
        case default:
            print("Enter a valid choice")
            projectsMenu(userId)

mainMenu()