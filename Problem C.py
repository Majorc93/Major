while True:
    try:
        x = float(input("Enter a number: "))
        break
    except ValueError:
        print("ERROR: Invalid input")
while True:
    try:
        y = float(input("Enter another number: "))
        print("The sum is", x + y)
        break
    except ValueError:
        print("ERROR: Invalid input")