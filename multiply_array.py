def multiply_array(arra,arrb,arrc,m,n,p):
    global c
    if m<=0 or n<=0 or p<=0:
        print('m,n,p必須大於等於0')
        return
    for i in range(m):
        for j in range(p):
            Temp=0
            for k in range(n):
                Temp=Temp+int(arra[i*n+k])*int(arrb[k*p+j])
            arrc[i*p+j]=Temp

print('請輸入矩陣a的維度(m,n):')
m=int(input('m='))
n=int(input('n='))
a=[None]*m*n
print('請輸入a的各個元素')
for i in range(m):
    for j in range(n):
        a[i*n+j]=input('a[%d][%d]='%(i,j))

print('請輸入矩陣b的維度(n,p):')
n=int(input('n='))
p=int(input('p='))
b=[None]*n*p
print('請輸入a的各個元素')
for i in range(n):
    for j in range(p):
        b[i*p+j]=input('b[%d][%d]='%(i,j))
c=[None]*m*p
multiply_array(a,b,c,m,n,p)
print('result')
for i in range(m):
    for j in range(p):
        print('%d' %c[i*p+j],end='\t')
    print()