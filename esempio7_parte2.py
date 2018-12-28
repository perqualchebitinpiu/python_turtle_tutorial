# Author: Alfonso Breglia
# Email:  perqualchebitinpiu@gmail.com
# Date:   28/12/2018
# Description: parte 2 del programma che traccia i frattali
#

from turtle import Screen, Turtle, setup
import math

W = 600
H = 600


def grow(turtle, L, N):
    turtle.pencolor("brown")    #stiamo disegnando il tronco o il ramo e usiamo il colore marrone
    turtle.forward(L)

    if N == 0:                      #siamo a livello foglia
        turtle.pencolor("green")    #usiamo il colore verde per disegnare le foglie
        turtle.left(45)
        turtle.forward(L)
        turtle.backward(L)
        turtle.right(45)

        turtle.right(45)
        turtle.forward(L)
        turtle.backward(L)
        turtle.left(45)
        turtle.pencolor("brown")
    else:
        turtle.pencolor("brown")
        turtle.left(45)
        grow(turtle, L/2, N-1)
        turtle.right(45)

        turtle.right(45)
        grow(turtle, L/2, N-1)
        turtle.left(45)

    turtle.pencolor("brown")  #ci muoviamo sul tronco o sul  ramo e usiamo il colore marrone
    turtle.backward(L)


    
if __name__ == "__main__":

    setup(W,H)              #fissa le dimensioni dello schermo a 600 x 600 pixel

    myWin = Screen()        #crea lo schermo con il foglio da disegno 
    uga = Turtle()                 #popola il foglio con la tartaruga uga
    uga.left(90)
    uga.penup()
    uga.goto(0,-H/2+10)
    uga.pendown()
    grow(uga, 300, 6)

    myWin.exitonclick()  #aspetta il click del mouse
