# Author: Alfonso Breglia
# Email:  perqualchebitinpiu@gmail.com
# Date:   27/12/2018
# Description: programma di esempio che disegna un quadrato usando la tartaruga
#

from turtle import Screen, Turtle


if __name__ == "__main__":
    myWin = Screen()  #crea lo schermo con il foglio da disegno 
    uga = Turtle()    #popola il foglio con la tartaruga uga

    uga.forward(100)     #vai in avanti di 100
    uga.right(90)        #ruota di 90 gradi a destra

    uga.forward(100)     #vai in avanti di 100
    uga.right(90)        #ruota di 90 gradi a destra

    uga.forward(100)     #vai in avanti di 100
    uga.right(90)        #ruota di 90 gradi a destra

    uga.forward(100)     #vai in avanti di 100

    myWin.exitonclick()  #aspetta il click del mouse
