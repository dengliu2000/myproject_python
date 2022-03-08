numbers=[21,32,55,67,92,45,48]
even=[]
odd=[]
for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(sorted(even))
print(sorted(odd))