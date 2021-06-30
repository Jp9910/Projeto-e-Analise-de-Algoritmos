#Lista semanal de PAA - Lista 4 Questão 2
#Aluno: João Paulo Feitosa Secundo

def inversoes(vetor, n):
    temp_vetor = [0]*n
    return mergeCount(vetor, temp_vetor, 0, n-1)
 
def mergeCount(vetor, temp_vetor, left, right):
    
    qntInversoes = 0
    if left < right:
        mid = (left + right)//2
        qntInversoes += mergeCount(vetor, temp_vetor,left, mid)
        qntInversoes += mergeCount(vetor, temp_vetor,mid + 1, right)
        qntInversoes += merge(vetor, temp_vetor, left, mid, right)
    return qntInversoes

def merge(vetor, temp_vetor, left, mid, right):
    i = left
    j = mid + 1
    k = left
    qntInversoes = 0

    while i <= mid and j <= right:
        if vetor[i] <= vetor[j]:
            temp_vetor[k] = vetor[i]
            k += 1
            i += 1
        else:
            temp_vetor[k] = vetor[j]
            qntInversoes += (mid-i + 1)
            k += 1
            j += 1

    while i <= mid:
        temp_vetor[k] = vetor[i]
        k += 1
        i += 1

    while j <= right:
        temp_vetor[k] = vetor[j]
        k += 1
        j += 1

    for loop_var in range(left, right + 1):
        vetor[loop_var] = temp_vetor[loop_var]

    return qntInversoes
 
vetor = [1, 20, 6, 4, 5]
n = len(vetor)
resultado = inversoes(vetor, n)
print(resultado)

#O número de inversões de um vetor V de n elementos é o número de pares ordenados (i,j)
#tais que 1 ≤ i < j ≤ n e V[i] > V[j]. Escreva uma função que calcule o número de
#inversões de um vetor dado. O consumo de tempo de sua função deve ser O(n log n)

#(7,5) (7,4) (7,6) (13,5) (13,4) (13,6) (5,4) (18,4) (18,6)