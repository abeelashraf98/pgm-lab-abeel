a=int(input("Enter the number: "))
print("The factors of {} is:".format(a))
for i in range(1,a+1):
    if(a%i==0):
        print(i)