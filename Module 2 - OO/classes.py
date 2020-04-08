class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def isUnderAge(self):
        if self.age < 18:
            return True
        else:
            return False

class Admin(Person):
    pass

pessoa = Person("Yves", 26)
admin = Admin("Admin", 26)

def displayUser(user):
    print(f"Nome:{user.name}\nIdade:{user.age}")
    print("É menor de idade") if user.isUnderAge() else print("É maior de idade")

displayUser(pessoa)
displayUser(admin)