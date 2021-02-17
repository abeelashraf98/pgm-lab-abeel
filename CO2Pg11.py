a=int(input("Enter length:"))
b=int(input("Enter breath:"))
c=int(input("Enter height of triangle:"))
sq=lambda a:a**2
rect=lambda a,b:a*b
tri=lambda b,c:(0.5*b*c)
print("Area of square : ",sq(a))
print("Area of Rectangle : ",rect(a,b))
print("Area of Triangle : ",tri(b,c))

