inp=raw_input("enter correct filename")
inp2=raw_input("enter parser o/p")
	
f=open(inp)
a=f.readlines()
f.close()

f=open(inp2)
b=f.readlines()
f.close()

x=[]
for i in range(0,50):
	x.append(0)


y=[]
for i in range(0,50):
	y.append(0)
countw=0
startsentence = 0
wrong=0
assert (len(a)==len(b))

for i in range(len(a)):
	if a[i] == '\n':
		assert(b[i]=='\n')
		for j in range(startsentence,i):
			temp=abs(int(a[j].split()[0]) - int(a[j].split()[6]))
			assert temp>0 
			assert temp <50

			if a[j]==b[j]:
				x[temp]+=1

			y[temp]+=1
		startsentence=i+1

for i in range(len(x)):
	if y[i]!=0:
		print i,x[i]/float(y[i])
