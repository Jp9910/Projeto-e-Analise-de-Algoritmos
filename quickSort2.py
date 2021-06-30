
import random

def quickSort (lista,inicio=0,fim=None):
    if fim is None:
        fim = len(lista)-1
    if (inicio < fim):
        pivot = particao(lista,inicio,fim)
        quickSort(lista,inicio,pivot-1)
        quickSort(lista,pivot+1,fim)

def particao (lista,inicio,fim):
    pivot = lista[fim] #Por convençao, pivot será o ultimo elemento
    i = inicio #barraAmarela - Tudo que é menor que o pivot fica a sua esquerda
                #avança quando encontra um elemento menor que o pivot
    j = 0 #barraAzul - Tudo que é maior que o pivot - Avança a cada passo
    for j in range (inicio,fim): #indice fim é onde está o pivot
        if (lista[j] <= pivot): #Se o numero na posiçao da barra azul for menor que o pivot..
            lista[j], lista[i] = lista[i], lista[j] #Troca a posiçao do elemento da barra roxa com o elemento da barra amarela
            i = i + 1
        #Se o numero na posiçao da barra azul for maior, nao precisa fazer nada
    lista[i],lista[fim] = lista[fim], lista[i] #Por fim, troca-se a posiçao do pivot para sua posiçao correta
    return i #retorna a posiçao do pivot


teste = random.sample(range(1,1000),42)
print(teste)
quickSort(teste)
print("\n\n\n",teste)