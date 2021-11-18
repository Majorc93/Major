try:
    x = input("Enter a filename: ")
    filename = open(x, "r")
    diction = open("dict.txt", "r")
    readfile = diction.read()
    index = 0
    for i in filename:
        index += 1
        y = i.lower().replace(",", "").replace(".", "").strip().split()
        z = i.replace(",", "").replace(".", "").strip().split()
        j = 0
        while j < len(y):
            if y[j] not in readfile.lower().split():
                print(f"Line {index}:", z[j])
            j += 1
except FileNotFoundError:
    print("Error: Cannot open the file")