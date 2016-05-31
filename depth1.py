inp=raw_input("enter correct filename")
inp2=raw_input("enter parser op")

depth=input("enter depth")

f=open(inp)
a=f.readlines()
f.close()

f=open(inp2)
b=f.readlines()
f.close()

CC=0
Ccount=0
gaga=0
startsentence=0
for i in range(len(a)):
	if a[i] == '\n':
		assert(b[i]=='\n')

		list1=[]
		start=-1
		for j in range(startsentence,i):
			if "0	main" in a[j]:
				start= j-startsentence
		assert(start >= 0)

		tempdepth=depth	
		list1.append(a[start+startsentence])

		while tempdepth > 0:
			tempdepth-=1
			for j in range(startsentence,i):
				for k in list1:	
					if k.split()[0] == a[j].split()[6]:
						if a[j] not in list1:
							list1.append(a[j])


		list2=[]
		start=-1
		for j in range(startsentence,i):
			if "0	main" in b[j] or "ROOT" in b[j]:
				start= j-startsentence


		assert(start >= 0)

		tempdepth=depth	
		list2.append(b[start+startsentence])
		
		while tempdepth > 0:
			tempdepth-=1
			for j in range(startsentence,i):
				for k in list2:	
#			print list2
					if k.split()[0] == b[j].split()[6]:
						if b[j] not in list2 and b[j]!='\n':
							list2.append(b[j])


		for l in list1:
			if l in list2:
				Ccount+=1
				
		CC+=len(list1)


		startsentence=i+1
	else:
		if "ROOT" in b[i] and b[i].split()[3]!="punc":
#if a[i]!=b[i]:
#				if b[i].split()[7]=="ROOT":
				
			Ccount+=1
			gaga+=1
		

#print gaga
#print Ccount
#print CC
print
print depth,Ccount/float(CC)
		


