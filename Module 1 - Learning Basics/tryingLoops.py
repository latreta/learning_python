myString = "TESTING"

print("Looping through each Character from String")
# for x in myString:
#     print(x)

print("From 0 to less than 6")
# for x in range(6):
#     print(x)


print("From 2 to less than 6")
# for x in range(2, 6):
#     print(x)


print("From 2 to less than 30 adding 3 at each loop")
# for x in range(2, 30, 2):
#    print(x)

i = 1
length = 10
print(f"Using While Loops, looping from {i} to less than {length}")
while i < length:
    print(i)
    if i == 15: # Testing break statement
        break
    i += 1


names = []
opcao = 1
while opcao == 1:
    name = str(input("Digite um nome: "))
    names.append(name)
    opcao = int(input("Se quiser adicionar mais, digite 1, caso contrário, digite 0: "))
print(names)