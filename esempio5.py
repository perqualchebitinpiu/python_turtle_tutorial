# Author: Alfonso Breglia
# Email:  perqualchebitinpiu@gmail.com
# Date:   28/12/2018
# Description: programma che disegna un poligono regolare 
#

from turtle import Screen, Turtle, setup
import math

W = 600
H = 600
N = 200

#disegna un poligono regolare: N è il numero di lati e L è la lunghezza del lato
def draw_poly(turtle, N, L):    

    for l in range(N):          
        turtle.forward(L)       #disegna un lato 
        turtle.left(360/N)      #ruota verso sinistra di un angolo 360/N 
    
if __name__ == "__main__":

    setup(W,H)              #fissa le dimensioni dello schermo a 600 x 600 pixel

    myWin = Screen()        #crea lo schermo con il foglio da disegno 
    uga = Turtle()                 #popola il foglio con la tartaruga uga
    
    #disegna tre poligoni
    draw_poly(uga, 3, 60)       #disegna un triangolo di lato 60
    uga.home()                  #torna al centro
    uga.pencolor("red")         #cambia colore
    draw_poly(uga, 4, 60)       #disegna un quadrato di lato 60
    uga.home()                  #torna al centro
    uga.pencolor("yellow")
    draw_poly(uga, 5, 60)       #disegna un pentagono di lato 60
    uga.home()                  #torna al centro
    uga.pencolor("blue")
    draw_poly(uga, 6, 60)       #disegna un esagono di lato 60
    uga.home()                  #torna al centro
    uga.pencolor("green")
    draw_poly(uga, 7, 60)       #disegna un eptagono di lato 60
    uga.home()                  #torna al centro
    uga.pencolor("pink")
    draw_poly(uga, 8, 60)       #disegna un ottagono di lato 60
    uga.home()                  #torna al centro
    uga.pencolor("orange")      #disegna un poligono regolare di 30 lati 
    draw_poly(uga, 30, 30)      #questo poligono assomiglia ad un cerchio

    myWin.exitonclick()  #aspetta il click del mouse
