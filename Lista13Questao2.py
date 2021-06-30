#Lista semanal de PAA - Lista 13 Questão 2
#Aluno: João Paulo Feitosa Secundo

import random

def escolhaJusta(): #51%=1 e 49%=0
    #b = [-1]*9
    cont=0
    for i in range(0,9):
        b = escolha() #60%=0 e 40%=1
        if(b==1):
            cont=cont+1
    #print(b)
    if(cont>=4):
        return 1
    else:
        return 0

def escolha():
    a = random.randint(1,10)
    if(a>=7): #7,8,9,10
        return 1
    else: #1,2,3,4,5,6
        return 0

x = escolhaJusta()
print(x)

#x = (0.6**9) + (0.4*(0.6**8)) + ((0.4**2)*(0.6**7)) + ((0.4**3)*(0.6**6)) + ((0.4**4)*(0.6**5)) + ((0.4**5)*(0.6**4)) + ((0.4**6)+(0.6**3)) + ((0.4**7)+(0.6**2)) + ((0.4**8)*(0.6**1)) + (0.4**9)
