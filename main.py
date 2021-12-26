from turtle import Turtle,Screen
import random
v=Turtle()
i=Turtle()
b=Turtle()
g=Turtle()
y=Turtle()
o=Turtle()
r=Turtle()
s=Screen()
s.setup(width=500,height=500)
ip=s.textinput("Input","Enter the rainbow colored turtle which you want to bet on in small case")
v.shape("turtle")
v.color("violet")
v.penup()
v.goto(-240,220)
v.pendown()

i.shape("turtle")
i.color("indigo")
i.penup()
i.goto(-240,150)
i.pendown()

b.shape("turtle")
b.color("blue")
b.penup()
b.goto(-240,80)
b.pendown()

g.shape("turtle")
g.color("green")
g.penup()
g.goto(-240,10)
g.pendown()

y.shape("turtle")
y.color("yellow")
y.penup()
y.goto(-240,-80)
y.pendown()

o.shape("turtle")
o.color("orange")
o.penup()
o.goto(-240,-150)
o.pendown()

r.shape("turtle")
r.color("red")
r.penup()
r.goto(-240,-220)
r.pendown()

while True:
    v.forward(random.randint(1,10))
    i.forward(random.randint(1,10))
    b.forward(random.randint(1,10))
    g.forward(random.randint(1,10))
    y.forward(random.randint(1,10))
    o.forward(random.randint(1,10))
    r.forward(random.randint(1,10))

    if v.position()[0]>=240:
        print("The violet turtle wins")
        val="violet"
        break

    if i.position()[0]>=240:
        print("The indigo turtle wins")
        val="indigo"
        break

    if b.position()[0]>=240:
        print("The blue turtle wins")
        val="blue"
        break

    if g.position()[0]>=240:
        print("The green turtle wins")
        val="green"
        break

    if y.position()[0]>=240:
        print("The yellow turtle wins")
        val="yellow"
        break
    if o.position()[0]>=240:
        print("The orange turtle wins")
        val="orange"
        break
    if r.position()[0]>=240:
        print("The red turtle wins")
        val="red"
        break

if val==ip:
    print("You win")
else:
    print("you loose")
    



s.exitonclick()