import re


def validateString(labelName):
    while True:
        value = input(f"Enter {labelName} ")
        if value.isalpha():
            break
        else:
            continue
    return value

def validateNumber(labelName):
    while True:
        value = input(f"Enter {labelName} ")
        if value.isdigit():
            value = int(value)
            break
        else:
            continue
    return value

def validateEmail():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    while True:
        value = input(f"Enter Email ")
        if re.fullmatch(regex, value):
            break
        else:
            continue
    return value

def validatePassword(): 
    regex = r'\b[A-Za-z0-9._%+-]{3,}\b'
    while True:
        value = input("Enter Your Password ")
        if re.fullmatch(regex, value):
            break
        else:
            continue
    return value

def confirmPassword(password): 
    while True:
        value = input("Enter Your Password confirmation ")
        if password == value:
            break
        else:
            continue
    return value


def validatePhone(): 
    regex = r'^201[0125][0-9]{8}$'
    while True:
        value = input("Enter Phone number starts with 201 ")
        if re.fullmatch(regex, value):
            break
        else:
            continue
    return value