# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
vehicles = ("Car", "Airplane", "Motorcycle")


def lastItem(vehicles):
    print(vehicles[-1])

def changeValue(newValue, index, vehicles):
    vehiclesList = list(vehicles)
    vehiclesList[index] = newValue
    vehicles = tuple(vehiclesList)

def checkIfExists(value, vehicles):
    if value in vehicles:
        print(f"Yes, {value} is in vehicles lists")