import turtle

turtle.setup(1000, 1000)
turtle.speed(0)

data = []

with open("picture.txt") as my_file:
    for line in my_file:
        try:
            x, y = line.split(",")
            data.append((int(x), int(y)))
        except ValueError:
            data.append((0, 0))
turtle.penup()
for i in data:
    if i == (0, 0):
        turtle.penup()
        continue
    turtle.setpos(i)
    turtle.pendown()

turtle.done() 
