# Author: Alfonso Breglia
# Email:  perqualchebitinpiu@gmail.com
# Date:   27/12/2018
# Description: programma di esempio che disegna ilgrafico di una funzione matematica
#

from turtle import Screen, Turtle, setup
import math

W = 600
H = 600
N = 200

if __name__ == "__main__":

    setup(W,H)              #fissa le dimensioni dello schermo a 600 x 600 pixel

    myWin = Screen()        #crea lo schermo con il foglio da disegno 
    uga = Turtle()                 #popola il foglio con la tartaruga uga

    # traccia la riga dell'asse delle ascisse
    uga.penup()                    #tira su la penna
    uga.setheading(180)            #gira la tartaruga verso ovest (non è necessario)
    uga.goto(-W/2,0)               #spostati al bordo sinistro
    uga.pendown()                  #metti la penna sul foglio
    uga.setheading(0)              #gira la tartaruga verso est (non è necessario)
    uga.goto(W/2,0)                #traccia la linea fino al bordo destro
    #traccia l'asse delle ordinate 
    uga.penup()                    #tira su la penna 
    uga.goto(0,-W/2)               #spostati al bordo inferiore al centro
    uga.setheading(90)            #gira la tartaruga verso Nord (non è necessario)
    uga.pendown()                  #metti la penna sul foglio
    uga.goto(0,W/2)                #traccia la linea fino al bordo superiore


    #spostati al bordo sinistro per iniziare a tracciare il grafico
    uga.penup()
    uga.goto(-W/2,0)
    uga.pendown()
    uga.pencolor("blue")

    for i in range(N):
        x = i*W/N-W/2           #calcola la coordinata X   
        y = 250*math.sin(2*math.pi*10*x/W)*math.cos(math.pi*x/W)    #calcola la coordinata y
        uga.goto(x,y)     # vai a x,y

    myWin.exitonclick()  #aspetta il click del mouse
