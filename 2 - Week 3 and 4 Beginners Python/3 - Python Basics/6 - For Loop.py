expenses = [1200, 1300, 1500, 1700]

total_expenses = expenses[0] + expenses[1] + expenses[2] + expenses[3]

print(total_expenses)

#For Loop
expenses = [1200, 1300, 1500, 1700, 1800, 2400]

total_expense = 0  #Initialisation
for expense in expenses:
    total_expense = total_expense + expense
print(total_expense)

#range
expenses = [1200, 1300, 1500, 1700]
total_expense = 0  #Initialisation
for i in range(len(expenses)):
    expense = expenses[i]
    print(f'Month {i+1}, Expense: {expense} ')
    total_expense = total_expense + expense
print("Total Expense:", total_expense)

#Enumeration
expenses = [1200, 1300, 1500, 1700]
total_expense = 0  #Initialisation
for i, expense in enumerate(expenses):
    print(f'Month {i+1}, Expense: {expense} ')
    total_expense += expense
print("Total Expense:", total_expense)

#BreakPoint
expenses = [1200, 1300, 2100, 1700, 2300]
for i, expenses in enumerate(expenses):
    if  expenses > 2000:
        print(f'Month {i+1} has expense > 2000')
        break

locations = ["sofa", "garage", "chair", "table", "closet"]
key_location = "chair"
for location in locations:
    if location == key_location:
        print("Key is found at ", location)
        break
    else:
        print("Key is not found at ", location)

for i in range(1, 11):
    if i % 2 == 1:
        print(i)

#Continue
for i in range(1, 11):
    if i % 2 == 0:
            continue
    print(i)

#While loop
n = 0
while n<=10:
    print(n)
    n += 1
# Use for loop as much compared to While Loop
