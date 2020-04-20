def handleName(name):
    return name.replace("\n","")

def readFile(fileName):
    f = open(fileName, "rt")
    names = []
    for name in f:
        names.append(handleName(name))
    f.close()
    return names


_fileName = "names.txt"

print(readFile(_fileName))