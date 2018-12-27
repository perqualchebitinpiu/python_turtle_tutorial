# Author: Alfonso Breglia
# Email:  perqualchebitinpiu@gmail.com
# Date:   27/12/2018
# Description: programma di esempio che disegna un esagono colorato usando la tartaruga
#

from turtle import Screen, Turtle


if __name__ == "__main__":
    myWin = Screen()        #crea lo schermo con il foglio da disegno 
    uga = Turtle()          #popola il foglio con la tartaruga uga

    uga.pencolor("red")     #usa la penna rossa
    uga.forward(100)        #vai in avanti di 100
    uga.right(60)           #ruota di 60 gradi a destra

    uga.pencolor("blue")    #usa la penna rossa
    uga.forward(100)        #vai in avanti di 100
    uga.right(60)           #ruota di 60 gradi a destra

    uga.pencolor(0,1.0,0)   #usa la penna verde secondo la notazione rgb
    uga.forward(100)        #vai in avanti di 100
    uga.right(60)           #ruota di 60 gradi a destra

    uga.pencolor("#33cc8c") #usa la penna verde secondo la notazione rgb stringa
    uga.forward(100)        #vai in avanti di 100
    uga.right(60)           #ruota di 60 gradi a destra

    uga.pencolor("black")   #usa la penna nera
    uga.forward(100)        #vai in avanti di 100
    uga.right(60)           #ruota di 60 gradi a destra

    uga.pencolor("orange")   #usa la penna arancione
    uga.forward(100)        #vai in avanti di 100


    myWin.exitonclick()  #aspetta il click del mouse
