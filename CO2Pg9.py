a=int(input("Enter the number"))
for i in range(1,a+1):
    for i in range(1,i+1):
        print("*",end="")
    print("\r")
for i in reversed(range(1,a)):
    for i in reversed(range(1,i+1)):
        print("*",end="")
    print("\r")