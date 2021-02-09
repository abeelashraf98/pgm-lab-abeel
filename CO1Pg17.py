y={'a':8,'d':2,'f':3,'g':6,'b':0,'c':17,'e':9}
print("Dictionary:",y)
l=list(y.items())
l.sort()
print('Ascending order is',l)
l=list(y.items())
l.sort(reverse=True)
print('Descending order is',l)