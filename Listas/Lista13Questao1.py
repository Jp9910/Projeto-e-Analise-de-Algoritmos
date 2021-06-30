#Lista semanal de PAA - Lista 13 Questão 1
#Aluno: João Paulo Feitosa Secundo
import random
import time
#https://www.geeksforgeeks.org/try-except-vs-if-in-python/

def senhaForte():
    senhaValida = False
    while(not senhaValida):
        tamanho = random.randint(8,14)
        caracteres = ['']*tamanho
        for i in range(0,tamanho):
            aleatorio = random.randint(0,len(alfabeto)-1)
            letra = alfabeto[aleatorio]
            #letra = random.choice(alfabeto)#escolher aleatoriamente um elemento
            caracteres[random.randint(0,tamanho-1)] = letra
        senha = ''
        senha = senha.join(caracteres)
        print("Senha:\"",senha,"\"",end=' --> ')
        senhaValida=validarSenhaForteD(senha,len(senha))
        print("Válida?",senhaValida)
    print("\nSenha Forte: \" %s \""%senha)

"""
def validarSenhaForte(senha,n):
    if(n<8):
        return False
    contemLetraMin,contemLetraMai,contemNumero,contemSimbolo=False,False,False,False
    for i in range(n):
        if(senha[i] in simbolos):
            contemSimbolo=True
        elif(senha[i] in letrasMin):
            contemLetraMin=True
        elif(senha[i] in letrasMai):
            contemLetraMai=True
        elif(senha[i] in numeros):
            contemNumero=True
    if(contemSimbolo and contemLetraMin and contemLetraMai and contemNumero):
        return True
    else:
        return False
"""
def validarSenhaForteD(senha,n):
    if(n<8):
        return False
    contemLetraMin,contemLetraMai,contemNumero,contemSimbolo=False,False,False,False
    for i in range(n):
        if (senha[i] in simbolosD):
            contemSimbolo=True
        elif (senha[i] in letrasMinD):
            contemLetraMin=True
        elif (senha[i] in letrasMaiD):
            contemLetraMai=True
        elif (senha[i] in numerosD):
            contemNumero=True
    if(contemSimbolo and contemLetraMin and contemLetraMai and contemNumero):
        return True
    else:
        return False
"""
simbolos = ['!','@','#','$','%','^','&','*','(',')','-','_','+',',','.']

letrasMin = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',\
    's','t','u','v','w','x','y','z']

letrasMai = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',\
    'S','T','U','V','W','X','Y','Z']

numeros = ['0','1','2','3','4','5','6','7','8','9']
"""
alfabeto = ['!','@','#','$','%','^','&','*','(',')','-','_','+',',','.',\
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',\
    's','t','u','v','w','x','y','z'\
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',\
    'S','T','U','V','W','X','Y','Z',\
    '0','1','2','3','4','5','6','7','8','9']

simbolosD = {"!":1,"@":1,"#":1,"$":1,"%":1,"^":1,"&":1,"*":1,"-":1,"_":1}
letrasMinD = {'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,\
    'k':1,'l':1,'m':1,'n':1,'o':1,'p':1,'q':1,'r':1,\
    's':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1}
letrasMaiD = {'A':1,'B':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'J':1,\
    'K':1,'L':1,'M':1,'N':1,'O':1,'P':1,'Q':1,'R':1,\
    'S':1,'T':1,'U':1,'V':1,'W':1,'X':1,'Y':1,'Z':1}
numerosD = {'0':1,'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1}


senhaForte()