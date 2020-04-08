class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def isUnderAge(self):
        if self.age < 18:
            return True
        else:
            return False


pessoa = Person("Yves", 26)

print(pessoa.name)
print(pessoa.age)
print(pessoa.isUnderAge())