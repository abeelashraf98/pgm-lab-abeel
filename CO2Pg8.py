a=int(input("Enter a limit:"))
l1=[]
l2=[]
print("Enter the words")
for i in range(0,a):
    l1.append(input())
print("The length of longest word")
for i in range(0,a):
    l2.append(len(l1[i]))
    k=max(l2)
print(k)
    
    

    