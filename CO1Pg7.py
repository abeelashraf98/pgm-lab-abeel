list1=[2,5,7]
list2=[2,7,3,12]
if(len(list1)==len(list2)):
    print("List are same length")
else:
    print("List are diffrent length")
s=0
k=0
for x in range(0,len(list1)):
    s=s+list1[x]
for x in range(0,len(list2)):
    k=k+list2[x]
if(s==k):
    print("Sums are same")
else:
    print("Sums are diffrent")
m=[]
for x in range(0,len(list1)):
               for j in range(0,len(list2)):
                   if(list1[x]==list2[j]):
                       m.append(list1[x] and list2[j] )
print("Matching Elements are:")
print(m)