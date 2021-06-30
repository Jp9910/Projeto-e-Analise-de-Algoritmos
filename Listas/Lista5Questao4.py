#Lista semanal de PAA - Lista 5 Questão 4
#Aluno: João Paulo Feitosa Secundo

def countingSort(A,n,k):
    C = [0] * (k+1)
    repeticoes=0
    for i in range(0,k+1):
        C[i] = 0
    for j in range(0,n):
        repeticoes+=C[A[j]]
        C[A[j]] += 1
        #if(C[A[j]] >= 2):
        #    repeticoes+=C[A[j]]-1
    return repeticoes

A = [1,5,3,4,4,5,5,2,1,1,1,5,1,0,0]
n = len(A)
maior=max(A)
resultado = countingSort(A,n,maior)
print(resultado)