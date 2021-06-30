
def somarMatrizes (matrix1,matrix2,n):
    resultado=[[0,0,0],\
               [0,0,0],\
               [0,0,0]]
    for i in range(0,n):
        for j in range(0,n):
            resultado[i][j] = matrix1[i][j] + matrix2[i][j]
    
    print (resultado)

matrix1=[[1,3,5],\
        [7,9,11],\
        [13,15,17]]

matrix2=[[0,2,4],\
        [6,8,10],\
        [12,14,16]]

somarMatrizes(matrix1,matrix2,3);