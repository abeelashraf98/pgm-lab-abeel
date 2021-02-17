a=int(input("Enter The Number:"))
fact=1
print("Factorial Of Number{} is :".format(a))
for i in range(1,a+1):
    fact=fact*i
print(fact)