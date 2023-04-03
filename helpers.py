

def readFromFile(file):
    try:
        fileObj = open(file, 'r')
        pass
    except Exception as e:
        print(e)
    else: 
        data = fileObj.readlines()
        fileObj.close()
        return data

def writeIntoFile(file, content):
    try:
        fileObj = open(file, 'a')
        pass
    except Exception as e:
        print(e)
    else: 
        fileObj.writelines(content)
        fileObj.close()
        print("Data Added Successfully")
