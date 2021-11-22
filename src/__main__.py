import turtle
import time
#skrin
sc = turtle.Screen()
sc.setup(500, 700)
sc.bgcolor("black")
sc.title("igrica")
sc.tracer(0)

zivljenja = 3
switch = 0

#rezultat
rez = turtle.Turtle()
rez.hideturtle()
rez.color("white")

#odstevanje
ods = turtle.Turtle()
ods.color("white")
ods.hideturtle()

#obroba
obr_L = turtle.Turtle()
obr_L.color("white")
obr_L.penup()
obr_L.goto(-240, 0)
obr_L.shape("square")
obr_L.shapesize(stretch_wid=35, stretch_len=1)

#ovira
ovira = turtle.Turtle()
ovira.shape("square")
ovira.color("white")
ovira.penup()
ovira.goto(0, 100)
ovira.shapesize(6, 1)

obr_Z = turtle.Turtle()
obr_Z.color("white")
obr_Z.penup()
obr_Z.goto(0, 340)
obr_Z.shape("square")
obr_Z.shapesize(stretch_wid=1, stretch_len=24)

obr_D = turtle.Turtle()
obr_D.color("white")
obr_D.penup()
obr_D.goto(230, 0)
obr_D.shape("square")
obr_D.shapesize(stretch_wid=35, stretch_len=1)

#lopar
lopar = turtle.Turtle()
lopar.speed(0)
lopar.shape("square")
lopar.shapesize(stretch_wid=1, stretch_len=5)
lopar.color("white", "black")
lopar.penup()
lopar.goto(0, -270)


#zogia
zogica = turtle.Turtle()
zogica.speed(0)
zogica.penup()
zogica.goto(0, 200)
zogica.shape("circle")
zogica.color("white")
zogica.dx = 0.8
zogica.dy = -0.8

def lopar_levo():
    x = lopar.xcor()
    x -= 30
    lopar.setx(x)
def lopar_desno():
    x = lopar.xcor()
    x += 30
    lopar.setx(x)

for i in range(3, 0, -1):
    ods.write(f"Start in : {i}", align="center", font=["Courier", 20])
    time.sleep(1)
    ods.clear()
rez.write(f"Imaš še {zivljenja} življenja ", align="center", font=["Courier", 15])

sc.listen()
sc.onkeypress(lopar_levo, "a")
sc.onkeypress(lopar_desno, "d")


#glavna zanka
while True:


    sc.update()


    zogica.setx(zogica.xcor() + zogica.dx)
    zogica.sety(zogica.ycor() + zogica.dy)

    if zogica.xcor() > 220:
        zogica.dx *= -1

    if zogica.xcor() < -220:
        zogica.dx *= -1

    if zogica.ycor() < -280:
        zogica.goto(0, 200)
        zivljenja -= 1
        rez.clear()
        rez.write(f"Imaš še {zivljenja} življenja ", align="center", font=["Courier", 15])

    if zogica.ycor() > 310:
        zogica.dy *= -1

    if zogica.ycor() < -270 and zogica.ycor() < -260  and (zogica.xcor() < lopar.xcor() +50 and zogica.xcor() > lopar.xcor() -50):
        switch += 1
        zogica.dy *= -1
        if switch%2 != 0:
            lopar.color("white")
        else:
            lopar.color("white", "black")
    if (zogica.xcor() < ovira.xcor() + 15 and zogica.xcor() > ovira.xcor() -15) and (zogica.ycor() < ovira.ycor() + 65 and zogica.ycor() > ovira.ycor() -65):
        zogica.dx *= -1

    if zivljenja == 0:
        break

