from validation import validateEmail, validatePassword, confirmPassword, validateString, validatePhone
from helpers import readFromFile, writeIntoFile
import time


def register():
    email = "" 
    users = readFromFile("./data/users.txt")
    while True:
        isFound = False
        email = validateEmail()
        for user in users:
            if email == user.strip("\n").split(":")[1] : 
                isFound = True
                print("Email Already exists")
                break
        if isFound == False:
            break
        
    password = validatePassword()
    confirmPassword(password)
    firstName = validateString("First Name")
    lastName = validateString("Last Name")
    phone = validatePhone()
    id = round(time.time())




    content = f"{id}:{email}:{password}:{firstName}:{lastName}:{phone}\n"
    writeIntoFile("./data/users.txt",content)


def login():
    email = validateEmail()
    password = validatePassword()
    users = readFromFile("./data/users.txt")
    isFound = False
    for user in users:
        if email == user.strip("\n").split(":")[1] and  password == user.strip("\n").split(":")[2]: 
            isFound = True
            print("Logged In Successfully")
            return user.strip("\n").split(":")[0]
    if isFound == False:
        print("Invalid Credentials")
