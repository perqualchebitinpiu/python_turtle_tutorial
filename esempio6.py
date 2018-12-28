# Author: Alfonso Breglia
# Email:  perqualchebitinpiu@gmail.com
# Date:   28/12/2018
# Description: programma che disegna un cerchio
#

from turtle import Screen, Turtle, setup
import math

W = 600
H = 600


    
if __name__ == "__main__":

    setup(W,H)              #fissa le dimensioni dello schermo a 600 x 600 pixel

    myWin = Screen()        #crea lo schermo con il foglio da disegno 
    uga = Turtle()                 #popola il foglio con la tartaruga uga
    
    #disegna tre poligoni
    uga.circle(30,360)          #disegna un cerchio  completo di raggio 30
    uga.home()                  #torna al centro
    uga.pencolor("red")         #cambia colore
    uga.circle(40,360)          #disegna un cerchio completo di raggio 40
    uga.home()                  #torna al centro
    uga.pencolor("yellow")
    uga.circle(50,360)          #disegna un cerchio completo di raggio 50
    uga.home()                  #torna al centro
    uga.pencolor("blue")
    uga.circle(60,360)          #disegna un cerchio completo di raggio 60
    uga.pencolor("green")
    uga.circle(80,180)          #disegna un semi cerchio  di raggio 80


    myWin.exitonclick()  #aspetta il click del mouse
