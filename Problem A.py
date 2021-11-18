with open("input.txt", "r") as input:
    with open("output.txt", "w") as output:
        for line in input:
            output.write(line[0].upper())
            output.write(line[1:])