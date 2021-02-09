a =int(input("Enter the first no:"))
b=int(input("Enter the second no"))
for i in range(1,min(a,b)+1):
  if(a%i==0 and b%i==0):
    gcd=i
print("GCD of ",a,"and",b,"is",gcd)
