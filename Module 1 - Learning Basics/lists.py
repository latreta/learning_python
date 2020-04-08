# List is a collection which is ordered and changeable. Allows duplicate members.
vehicles = ["Motorcycle", "Car", "Bus"]

def printLastItem(array):
    print(f"The last item from array is: {array[-1]}") # Acessing the last item from list

def replaceValueAt(array, value, index):
    if len(array) > index:
        array[index] = value

def addItemAt(array, value, index):
    array.insert(index, value)

def addItem(array, value):
    array.append(value)

def getVehiclesCount(array):
    print(f"Vehicles list has {len(vehicles)} vehicles.")

def isVehicleAdded(vehicles, vehicle):
    if vehicle in vehicles:
        print(f"Yes, {vehicle} exists at vehicles list.")
        pass
    else:
        print("No")
        pass

# functions = {
#     0: printLastItem,
#     1: replaceValueAt,
#     2: addItemAt,
#     3: addItem,
#     4: getVehiclesCount,
#     5: isVehicleAdded
# }

# printLastItem(vehicles)
# replaceValueAt(vehicles, "Airplane", 1)
# addItemAt(vehicles, "Car", 1)
# getVehiclesCount(vehicles)
# isVehicleAdded(vehicles, "Airplane")