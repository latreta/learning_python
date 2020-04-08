class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.admin = False

    def isUnderAge(self):
        if self.age < 18:
            return True
        else:
            return False
    
    def isAdmin(self):
        return self.admin

class Admin(Person):
    def __init__(self, name, age, ):
        super().__init__(name, age)
        self.admin = True
    

pessoa = Person("Yves", 26)
admin = Admin("Admin", 26)

def displayUser(user):
    print(f"Nome:{user.name}\nIdade:{user.age}")
    print("É menor de idade") if user.isUnderAge() else print("É maior de idade")
    print("Tem privilegios de admin") if user.isAdmin() else print("Nao tem privilegios de admin")

displayUser(pessoa)
displayUser(admin)