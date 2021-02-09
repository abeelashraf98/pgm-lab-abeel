a=input("Enter a word")
count=0
for j in range(0,len(a)):
    if(j==0):
        print(a[j],end="")
    else:
        if(a[0]==a[j]):
            print("$",end="")
        else:
            print(a[j],end="")

    
            
               