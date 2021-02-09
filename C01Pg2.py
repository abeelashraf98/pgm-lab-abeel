a=int(input("Enter the Final year: "))
i=2021
print("Leap Years Between {} and {} are".format(i,a))
while i<=a:
    flag=0
    while(i%100==0 and i%400==0 or i%4==0):
        flag=1
        break
    if(flag==1):
        print(i)
    i=i+1
        
        
        
