import turtle
whatcolor = str(input("What color do you want?"))

turtle.bgcolor("black")

sides = 2
for x in range(200):
    turtle.pencolor(whatcolor)
    turtle.forward(x)
    turtle.right(300)
    turtle.speed(100)
    turtle.width(5)
    
    
    
