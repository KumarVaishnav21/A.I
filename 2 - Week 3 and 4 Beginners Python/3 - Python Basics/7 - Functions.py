# Normal way of doing it
expenses_surgey = [30, 45, 70, 90]
expenses_sundar = [40, 23, 10, 85]

total = 0

for expense in expenses_surgey:
    total  = total + expense

print("Surgey's total expense: ", total)

for expense in expenses_sundar:
    total = total + expense

print("Sundar's total expense: ", total)

#Using Function way of doing
def find_total(expenses):
    '''
    This function takes list as an input
    and return a total sum of that list
    :param expenses:
    :return:
    '''
    total = 0
    for expense in expenses:
        total += expense
    return total


expenses_surgey = [30, 45, 70, 90]
expenses_sundar = [40, 23, 10, 85]

total = find_total(expenses_surgey)

print("Surgey's total expense: ", total)

total = find_total(expenses_sundar)

print("Sundar's total expense: ", total)

print(help(find_total))

#Volume of cyliner function
def find_cylinder_volumne(radius, height):
    print("radius:", radius)
    print("height:", height)
    return 3.14*(radius**2)*height


r = 5
h = 10

print(find_cylinder_volumne(r, h)) # Positional Argument
print(find_cylinder_volumne(radius = r, height = h)) #keyword Argument

#2
def find_cylinder_volumne(radius, height = 7):
    print("radius:", radius)
    print("height:", height)
    return 3.14*(radius**2)*height


r = 5
h = 10

print(find_cylinder_volumne(r)) # Positional Argument
print(find_cylinder_volumne(r, h)) # Positional Argument

#3
def find_cylinder_volumne(radius, height = 7):
    print("radius:", radius)
    print("height:", height)
    volume = 3.14*(radius**2)*height
    print("Volume is :", volume)
    return volume

r = 5
h = 10

print(find_cylinder_volumne(r, h)) # Positional Argument