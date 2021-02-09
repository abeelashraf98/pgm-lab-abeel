n=[]
s=int(input("Enter a limit:"))
print("Enter values")
for i in range(0,s):
    n.append(int(input()))
print("list values")
print(n)
print("The list after assigning:")
for i in range(0,len(n)):
    if n[i]>=100:
        n[i]="over"
print(n)
