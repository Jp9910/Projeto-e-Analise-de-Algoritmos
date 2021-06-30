def countingSort(A,B,n,k):
    C = [0] * (k+1) #+1 por causa que o elemento 0 precisa ser representado pelo indice 0
    for i in range(0,k+1):
        C[i] = 0
    for j in range(0,n):
        C[A[j]] += 1
    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]
    print(C)
    for j in range(n-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1

#A = [7,6,1,4,8,3,5,0,9,2]
A = [9,6,3,8,1,8,4,5,7,2,7,3,4,6,9,0,1,0,6,7,3]
B = [None]*len(A)
maior=0
for i in range(0,len(A)): 
    if(A[i]>maior): maior=A[i]
countingSort(A,B,len(A),maior)
print(B)

#C=[0,1,2,3,4,5,6,7,8,9]
#  [0,0,0,0,0,0,0,0,0,0]
#Na prática só se usa counting sort para k=n (não existem elementos repetidos)
#Counting sort só funciona para ordenar inteiros não negativos