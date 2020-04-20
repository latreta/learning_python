import os

_fileName = "names.txt"
breakline = "\n"

def handleName(name):
    return name.replace(breakline,"")

def readFile(fileName):
    f = open(fileName, "rt")
    names = []
    for name in f:
        names.append(handleName(name))
    f.close()
    return names

def addName(fileName, name):
    f = open(fileName, "at")
    f.write(name)
    f.write(breakline)
    f.close()

def deleteFile(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
    else:
        print("Arquivo nao existe")

addName(_fileName, "Teste")
print(readFile(_fileName))
#deleteFile(_fileName)