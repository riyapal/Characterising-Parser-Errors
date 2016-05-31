inp=raw_input("enter correct filename")
inp2=raw_input("enter parser op")

depth=input("enter depth")

f=open(inp)
a=f.readlines()
f.close()

f=open(inp2)
b=f.readlines()
f.close()


CC = [0]*20
Ccount = [0]*20

while depth > 0:
	depth-=1
	
	
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
					Ccount[depth]+=1
				
			CC[depth]+=len(list1)


			startsentence=i+1
	#	else:
	#		if "ROOT" in b[i] and b[i].split()[3]!="punc":
	#if a[i]!=b[i]:
	#				if b[i].split()[7]=="ROOT":
				
	#			Ccount[depth]+=1
				
		
print Ccount
print CC
	#print gaga
	#print Ccount
	#print CC
	#print
	#print depth,Ccount/float(CC)
		

for i in range(1,len(CC)):
#	print len(CC)-i-1
	CC[len(CC)-i]-=CC[len(CC)-1-i]
	Ccount[len(CC)-i]-=Ccount[len(CC)-1-i]


for i in range(len(CC)-1):
	if CC[i]!=0:
		print i,Ccount[i]/float(CC[i])


