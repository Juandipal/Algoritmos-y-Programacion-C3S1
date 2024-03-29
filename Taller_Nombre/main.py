  
import turtle
tortuga = turtle.Turtle()
colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange', 'pink','light blue',]

tortuga.pensize(9)
#Letra J
tortuga.pencolor("green")
tortuga.goto(120,0)
tortuga.goto(80,0)
tortuga.goto(80,-100)
tortuga.goto(-50,-50)
tortuga.penup()
#Letra U
tortuga.goto(120,-25)
tortuga.pendown()
tortuga.pencolor("blue")
tortuga.goto(120,-50)
tortuga.goto(120,-100)
tortuga.goto(170,-100)
tortuga.goto(170,0)
tortuga.penup()
#Letra A
tortuga.goto(210,-0)
tortuga.pendown()
tortuga.pencolor("green")
tortuga.goto(190,-100)
tortuga.penup()
tortuga.goto(210,0)
tortuga.pendown()
tortuga.goto(250,-100)
tortuga.penup()
tortuga.goto(190,-70)
tortuga.pendown()
tortuga.goto(250,-70)
tortuga.penup()
tortuga.goto(270,0)
#Letra N
tortuga.pendown()
tortuga.pencolor("purple")
tortuga.goto(270,-100)
tortuga.goto(270,0)
tortuga.goto(320,-100)
tortuga.goto(320,0)
tortuga.penup()
tortuga.goto(340,0)
#Letra D
tortuga.pendown()
tortuga.pencolor("green")
tortuga.goto(340,-100)
tortuga.goto(410,-70)
tortuga.goto(410,-20)
tortuga.goto(340,0)
tortuga.penup()

for i in range(20):
  tortuga.goto(-50,-130)
  tortuga.hideturtle
  tortuga.pendown()
  tortuga.color(colors[i%8])
  tortuga.forward (500)
  tortuga.left(90)
  tortuga.right(90)
  tortuga.speed(100)
tortuga.penup()
tortuga.goto(165,120)
tortuga.pendown()
tortuga.pensize(4)
for i in range(300):
  tortuga.color(colors[i%8])
  tortuga.forward(150)
  tortuga.left(150)
  tortuga.speed(100)