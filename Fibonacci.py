n = int(input("Please input a number:\n"))
total=i=1
while n<0:
        print("The number is invalid.")
        n = int(input("Please input a number:\n"))
        continue #當n為小於0的整數時,會重複執行此片段,要求使用者輸入整數值,直到n大於或等於0
if n==0:
   print("fac(0)=1") #當n等於0時,印出0!=1
else: #當n為大於0的整數時,執行n階層的運算
   while i<=n:
       total*=i
       i+=1
   print("fac(%d)=%d" %(n,total))