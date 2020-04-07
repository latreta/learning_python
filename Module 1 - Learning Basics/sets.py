# Set is a collection which is unordered and unindexed. No duplicate members.
vehicles = {"Car", "Motorcycle", "Boat"}
print(vehicles)

def checkIfExists(vehicle, vehiclesSet): 
    print(vehicle in vehiclesSet)

def addVehicle(vehicle, vehiclesSet):
    vehiclesSet.add(vehicle)

def addVehicles(items, vehiclesSet):
    vehiclesSet.update(items)

def removeVehicle(vehicle, vehiclesSet):
    vehiclesSet.discard(vehicle) # same from remove but doesn't raise error if dont exist

def createSet():
    mySet = set(("Red", "Blue", "Green"))
    print(mySet)