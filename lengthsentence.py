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
#	print "lala"
		y[countw]+=i-startsentence
		x[countw]+=wrong
		countw=0
		startsentence=i+1
		wrong=0
	else:
#	print "gaga"
		countw+=1
		if (a[i]) != (b[i]):
			wrong+=1

for i in range(50):
	if y[i]!=0:
		print str(i)+','+ str(1-(float(x[i])/y[i]))#,y[i],x[i]
