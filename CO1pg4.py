a=input("Enter a sentence")
d=dict()
s=a.split()
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
        
    