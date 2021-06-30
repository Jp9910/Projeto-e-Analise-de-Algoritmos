#Lista semanal de PAA - Lista 2 Questão 3
#Aluno: João Paulo Feitosa Secundo

def checarExpressao (exp,tamanho) -> bool:

    contAberto = 0
    abertos = []

    for i in range(0,tamanho):

        if (exp[i] == "[" or exp[i] == "("):
            abertos.append(exp[i])
            contAberto += 1
        
        elif (exp[i] == "]"):
            
            if(contAberto == 0): return False
            
            if(abertos[contAberto-1] == "["):
                abertos.pop(contAberto-1)
                contAberto-=1
            else: 
                return False

        elif (exp[i] == ")"):
            
            if(contAberto == 0): return False
            
            if(abertos[contAberto-1] == "("):
                abertos.pop(contAberto-1)
                contAberto-=1
            else: 
                return False

    if(contAberto == 0):
        return True
    else: return False

expressao1 = "[(a+b)+(c*d)]"
expressao2 = "]"

teste1 = checarExpressao(expressao1,len(expressao1))
teste2 = checarExpressao(expressao2,len(expressao2))

print("expressao 1: ",teste1)
print("expressao 2: ",teste2)