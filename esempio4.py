# Author: Alfonso Breglia
# Email:  perqualchebitinpiu@gmail.com
# Date:   28/12/2018
# Description: programma che disegna un rettangolo date le coordinate
#

from turtle import Screen, Turtle, setup
import math

W = 600
H = 600
N = 200

#disegna un rettangolo usando la tartaruga turtle
def draw_rect(turtle,  x1,y1, x2,y2):
    uga.penup()           #tira su la penna per spostarti sul vertice (x1,y1)
    uga.goto(x1,y1)       #spostati al vertice x1,y1
    uga.pendown()         #inizia a scrivere
    uga.goto(x1,y2)       #traccia il primo lato
    uga.goto(x2,y2)       #traccia il secondo lato
    uga.goto(x2,y1)       #traccia il terzo lato 
    uga.goto(x1,y1)       #traccia il quarto lato

if __name__ == "__main__":

    setup(W,H)              #fissa le dimensioni dello schermo a 600 x 600 pixel

    myWin = Screen()        #crea lo schermo con il foglio da disegno 
    uga = Turtle()                 #popola il foglio con la tartaruga uga
    
    #disegna tre rettangoli
    draw_rect(uga, -100,-50, 200,100) 
    draw_rect(uga, 10,15, 50,80)
    draw_rect(uga, 130, 148, -10, -60)


    myWin.exitonclick()  #aspetta il click del mouse
