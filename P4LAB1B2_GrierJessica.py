import turtle

t= turtle.Turtle()
t.Screen()

t.pensize(30)
t.pencolor('red')
t.shape('turtle')

t.forward(50)
t.backward(200)

t.right(90)
t.forward(180)

t.circle(-50,180)
t.penup()
t.goto(-30,50)
t.pendown()

t.right(180)
t.circle(50,180)
t.left(90)

t.forward(50)
t.goto(-50,0)
t.right(90)

t.forward(50)
t.right(90)
t.forward(20)
