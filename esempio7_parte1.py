# Author: Alfonso Breglia
# Email:  perqualchebitinpiu@gmail.com
# Date:   28/12/2018
# Description: parte 1 del programma che traccia i frattali
#

from turtle import Screen, Turtle, setup
import math

W = 600
H = 600


def grow(turtle, L):
    turtle.forward(L)

    turtle.left(45)
    turtle.forward(L/2)
    turtle.backward(L/2)
    turtle.right(45)

    turtle.right(45)
    turtle.forward(L/2)
    turtle.backward(L/2)
    turtle.left(45)
    
    turtle.backward(L)


    
if __name__ == "__main__":

    setup(W,H)              #fissa le dimensioni dello schermo a 600 x 600 pixel

    myWin = Screen()        #crea lo schermo con il foglio da disegno 
    uga = Turtle()                 #popola il foglio con la tartaruga uga
    uga.left(90)
    uga.penup()
    uga.goto(0,-H/2+10)
    uga.pendown()
    grow(uga, 300)

    myWin.exitonclick()  #aspetta il click del mouse
