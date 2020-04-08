# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

person = {
  "name": "Yves",
  "age": 26,
  "gender": "male"
}

def displayValues(user):
    for x in user:
        print(f"{x}: {user[x]}")

def displayBoth(user):
    for x,y in user.items():
        print(x, y)


def doesKeyExists(keyName, user):
    if keyName in user:
        print("True")

def addNewKey(keyName, keyValue, user):
    user[keyName] = keyValue

def removeKey(keyName, user):
    user.pop(keyName)

def clearDictionary(user):
    user.clear()