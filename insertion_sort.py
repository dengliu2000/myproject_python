def insertion_sort(arr):
    #插入排序第一次插入從第二個數字開始比較
    for i in range(1, len(arr)):
        #從選擇插入的資料，一次和它前一個比較，比前面的小就交換
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
    return arr
a=[7,5,3,2,1,-3,-5]
insertion_sort(a)
print("a:")
print(a)
b=[7.9,6.4,5.9,3,1]
insertion_sort(b)
print("b:")
print(b)
c=[13,9,9,7,7,4,2,1]
insertion_sort(c)
print("c:")
print(c)
