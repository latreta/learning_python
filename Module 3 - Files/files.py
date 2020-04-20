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
    f.write(breakline)
    f.write(name)
    f.close()

print(readFile(_fileName))
addName(_fileName, "Teste")
print(readFile(_fileName))