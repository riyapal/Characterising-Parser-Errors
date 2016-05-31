inp=raw_input("correct filename")
test=raw_input("parser o/p filename")
	
	
f=open(inp)
infile=f.readlines()
f.close()

f=open(test)
outfile=f.readlines()
f.close()
count=0
assert len(infile)==len(outfile)

for i in range(len(infile)):
	if infile[i]!='\n':
		if infile[i]!=outfile[i]:
			count+=1
	
'''	if infile[i]!='\n':
		print infile[i].split()[6]
		print outfile[i].split()[6]
		print
		if (infile[i].split()[6] != outfile[i].split()[6]) or (infile[i].split()[7] != outfile[i].split()[7]):

#		if infile[i]!=outfile[i]:
			count+=1'''
print count
print 1-(float(count)/(len(infile)-1910))
