a=int(input("Enter your 1st number"))
b=int(input("Enter your 2nd number"))
c=int(input("Enter your 3rd number"))
if a>b and a>c:
    print("The greatest number is {}".format(a))
if b>a and b>c:
    print("The greatest number is {}".format(b))
else:
     print("The greatest number is {}".format(c))
