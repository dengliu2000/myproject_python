import random

val=0
data=[0]*80
for i in range(80):
    data[i]=random.randint(1,150)
while val!=-1:
    find=0
    val=int(input('enter(1-150),exit(-1):'))
    for i in range(80):
        if data[i]==val:
            print('find %d in data[%d]'%(data[i],i+1))
            find+=1
    if find==0 and val !=-1 :
        print('Not find %d'%val)

print('data:')
for i in range(10):
    for j in range(8):
        print('data[%2d][%3d]'%(i*8+j+1,data[i*8+j]),end=' ')
    print('')