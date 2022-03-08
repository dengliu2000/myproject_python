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
