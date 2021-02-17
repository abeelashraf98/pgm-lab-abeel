a=int(input("Enter the no of terms:"))
count=0
for i in range(1,a+1):
    for j in range(1,i+1):
        k=i*j
        print(k,end=" ")
    print("\r")
        