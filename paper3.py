l=[]
a=int(input('enter number'))
str(a)
k=len(str(a))
f=1
for i in range(1,k+1):
	f=f*i
	l.append(str(i))

print(','.join(l))

