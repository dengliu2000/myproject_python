def bubble_sort(arr):
    #外迴圈為排列趟數，當陣列長度為len(arr)時，需排列len(arr)-1次
    for i in range(0, len(arr)-1):
        # 內迴圈為每趟比較次數，第i趟時比較len(arr)-i次
        for j in range(1, len(arr)-i):
            # 當前項大於後項時，則兩者進行交換
            if arr[j-1] < arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr
a=[5,3,4,1,7,2,6,8]
bubble_sort(a)
print("a:")
print(a)
def bubble_sort2(arr):
    for i in range(len(arr)-1,-1,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print('第%d次排序後的結果是:' %(len(arr)-i),end='')
        for j in range(len(arr)):
            print('%d' %arr[j],end='')
        print()
    print('排序後的結果:')
    for j in range(len(arr)):
        print('%d' %arr[j],end='')
    print()
bubble_sort2(a)