def ordenar(a,x,n):
    for i in range (n):
        t = x[a[i]-1]
        x[a[i]-1] = x[i]
        #x[i] = t

x = [17,5,1,9] #1,5,9,17
a = [3,2,4,1]
ordenar(a,x,len(x))
print(x)