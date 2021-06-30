#Lista semanal de PAA - Lista 13 Questão 3
#Aluno: João Paulo Feitosa Secundo

import random

def estimarPi():
    intervalo= 100
    pontosCirculo= 0
    pontosQuadrado= 0
    
    # Total Random numbers generated= possible x
    # values* possible y values
    for i in range(intervalo**2):
    
        # Randomly generated x and y values from a
        # uniform distribution
        # Range of x and y values is -1 to 1
        x= random.uniform(-1, 1)
        y= random.uniform(-1, 1)
    
        # Distance between (x, y) from the origin
        distanciaOrigem= x**2 + y**2
    
        # Checking if (x, y) lies inside the circle
        if distanciaOrigem<= 1:
            pontosCirculo+= 1
    
        pontosQuadrado+= 1
    
        # Estimating value of pi,
        # pi= 4*(no. of points generated inside the 
        # circle)/ (no. of points generated inside the square)
    pi = 4* pontosCirculo/ pontosQuadrado
    print(pi)
    #print(x, y, pontosCirculo, pontosQuadrado, "-", pi)
    #print("\n")
  
estimarPi()