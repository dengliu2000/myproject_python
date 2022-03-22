a=[[1,3,5],[7,9,11],[13,15,17]]
b=[[9,8,7],[6,5,4],[3,2,1]]
n=3
c=[[None]*n for row in range(n)]
for i in range(3):
    for j in range(3):
        c[i][j]=a[i][j]+b[i][j]
print('result')
for i in range(3):
    for j in range(3):
        print('%d' %c[i][j],end='\t')
    print()