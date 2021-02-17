a=input("Enter a sentence")
c=dict()
s=a.split()
print(s)
for x in s:
    if x in c:
        c[x]=c[x]+1
    else:
        c[x]=1
        
for key in list(c.keys()): 
    print("Frequency of",key, ":", c[key]) 
    

            
    