try:
    x = input("enter the name of a text file:")
    filename = open(x, "r")
    print(filename.read())
except FileNotFoundError:
    print("ERROR: File not found")