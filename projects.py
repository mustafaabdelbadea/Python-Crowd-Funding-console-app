from validation import validateString, validateNumber, validateDate
from helpers import readFromFile, writeIntoFile, overwrite
import time


def createPorject(user):
    title = validateString("Title")
    details = validateString("Details")
    totalTarget = validateNumber("Total target")
    startTime = validateDate("Start Date")
    endTime = validateDate("End Date")
    startValid = time.strptime(startTime, "%d-%m-%Y")
    endValid = time.strptime(endTime, "%d-%m-%Y")
    
    if startValid < endValid :
        projects = readFromFile("./data/projects.txt")
        if len(projects) == 0:
            row = f"User : ID : Title : Details : Total Target : Start Time : End Time \n"
            writeIntoFile("./data/projects.txt", row)

        id = round(time.time())
        content = f"{user}:{id}:{title}:{details}:{totalTarget}:{startTime}:{endTime}\n"
        writeIntoFile("./data/projects.txt",content)
    else:
        print("Invalid Start and end date")
        createPorject(user)

    



def getAllProjects():
    projects = readFromFile("./data/projects.txt")
    for project in projects:
        print(project.strip("\n").split(":"))
        

def editProject(user):
    id = validateNumber("Project ID")
    current = ""
    content = ""
    projects = readFromFile("./data/projects.txt")
    for project in projects:
        if project.strip("\n").split(":")[0] == user and int(project.strip("\n").split(":")[1]) == int(id):
            current = project.strip("\n").split(":")
            projects.remove(project)
            break

    choice = int(input("Enter\n1- Edit Title\n2- To Edit Details \n3- To Edit TotalTarget\n4- To Edit Start Date\n5- To Edit End Date "))

    match choice:
        case 1:
            title = validateString("Title")
            content = f"{user}:{id}:{title}:{current[3]}:{current[4]}:{current[5]}:{current[6]}"
        case 2:
            details = validateString("Details")
            content = f"{user}:{id}:{current[2]}:{details}:{current[4]}:{current[5]}:{current[6]}"
        case 3:
            target = validateNumber("Target")
            content = f"{user}:{id}:{current[2]}:{current[3]}:{target}:{current[5]}:{current[6]}"
        case 4:
            date = validateDate("Start Date")
            content = f"{user}:{id}:{current[2]}:{current[3]}:{current[4]}:{date}:{current[6]}"
        case 5:
            date = validateDate("End Date")
            content = f"{user}:{id}:{current[2]}:{current[3]}:{current[4]}:{current[5]}:{date[6]}"
        case default:
            print("Enter a valid choice ")

    projects.append(content)
    overwrite("./data/projects.txt", projects)
    print("Updated Successfully")


def deleteProject(user):
    id = validateNumber("Project ID")
    projects = readFromFile("./data/projects.txt")
    for project in projects:
        if project.strip("\n").split(":")[0] == user and int(project.strip("\n").split(":")[1]) == int(id):
            projects.remove(project)
            overwrite("./data/projects.txt", projects)
            print("Deleted Successfully")
            break
        

def searchForProject():
    projects = readFromFile("./data/projects.txt")
    choice = int(input("Enter\n1- To search by start date\n2- To search by end date \n"))
    search=""

    match choice:
        case 1:
            search = "start"
        case 2:
            search = "end"
        case default:
            print("Enter a valid choice ")

    date = validateDate("Date to search")
    for project in projects:
        if search == "start":
            if project.strip("\n").split(":")[6] == date:
                print(project.strip("\n").split(":"))
        else:
            if project.strip("\n").split(":")[5] == date:
                print(project.strip("\n").split(":"))
            
