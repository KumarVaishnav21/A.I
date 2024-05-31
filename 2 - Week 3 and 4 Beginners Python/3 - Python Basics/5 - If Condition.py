# # Check for Odd-Even *
n = input("Enter a number: ")
n = int(n)

if  n % 2 == 0:
    print("Number is even")
else:
   print("Number is odd")

# cuisine
indian = ["samosa", "daal", "naan"]
chinese = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

dish = input("Enter a dish name: ")

if dish in indian:
    print(f"{dish} is an Indian cuisine")
elif dish in chinese:
    print(f"{dish} is Shitty Chinese cuisine")
elif dish in italian:
    print(f"{dish} is an Italian cuisine")
else:
    print("I don't know which cuisine is this!")

# Check for Odd-Even  using Ternary operator*
n = input("Enter a number: ")
n = int(n)

message = "Number is even" if n % 2 == 0 else "Number is odd"
print(message)