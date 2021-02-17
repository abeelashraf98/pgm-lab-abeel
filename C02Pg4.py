from math import sqrt
a=int(input("Enter a limit greater than 1000: "))
for i in range(1000,a):
    k=sqrt(i)
    if(k==int(k) and i%2==0):
        print(i)
        

