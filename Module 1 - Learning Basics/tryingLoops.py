def displayMainMenuFunction():
    print("Welcome, what would you like to do? ")
    print("1 - Loop through all character from a String.")
    print("2 - Loop through array from 0 to Number.")
    print("3 - Loop from X to Y")
    print("4 - Loop from X to Y with new increase rate")
    print("5 - Loop using While using break")
    print("6 - Fill array with names.")
    print("0 - Sair do programa.")

def handleUserInput():
    opcao = int(input("Digite sua opcao: "))
    if opcao == 0:
        pass
    elif opcao == 1:
        loopThroughCharactersString("TESTING")
        pass
    elif opcao == 2:
        loopThroughArrayLessThan(6)
        pass
    elif opcao == 3:
        loopFromXtoY(0, 6)
        pass
    elif opcao == 4:
        loopFromXToYIncremented(2, 31, 2)
        pass
    elif opcao == 5:
        loopingThroughWhile(15, 10)
        pass
    elif opcao == 6:
        fillArrayUsingInput()
        pass

def loopThroughCharactersString(myText):
    print(f"Looping through each Character from String {myText}")
    for x in myText:
        print(x)

def loopThroughArrayLessThan(end):
    print(f"From 0 to less than {end}")
    for x in range(end):
        print(x)

def loopFromXtoY(start, end):
    print(f"From {start} to less than {end}")
    for x in range(start, end):
        print(x)

def loopFromXToYIncremented(start, end, incrementBy):
    print(f"From {start} to less than {end} adding {incrementBy} at each loop")
    for x in range(start, end, incrementBy):
        print(x)

def loopingThroughWhile(end, destinationToBreak):
    i = 1
    print(f"Using While Loops, looping from {i} to less than {end}")
    while i < end:
        print(i)
        if i == destinationToBreak: # Testing break statement
            break
        i += 1

def fillArrayUsingInput():
    names = []
    opcao = 1
    while opcao == 1:
        name = str(input("Digite um nome: "))
        names.append(name)
        opcao = int(input("Se quiser adicionar mais, digite 1, caso contrário, digite 0: "))
    print(names)

displayMainMenuFunction()
handleUserInput()