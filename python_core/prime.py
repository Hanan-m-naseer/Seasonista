n = int(input("enter a number: "))
flag = False
if n == 1 or n == 0:
    print("the number is not prime")
for i in range(2,n):
    if n % i == 0:
        flag = True
    break
if flag:
    print("the nember is not prime")
else:
    print("the number is prime")    
