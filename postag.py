f=open("goldintest_3_12")
a=f.readlines()
f.close()

f=open("goldoutmalt_3_12")
b=f.readlines()
f.close()
count=0
assert len(a)==len(b)

noun=0
ncount=0
adj=0
adjcount=0
psp=0
pspcount=0
adv=0
advcount=0
prp=0
prpcount=0
verb=0
vcount=0
conjunct=0
cccount=0
for i in range(len(a)):
		if a[i] !='\n':
			assert (b[i]!='\n')
			if "NN" in a[i]:
				noun+=1
				if a[i]==b[i]:
					ncount+=1
			
			elif "JJ" in a[i]:
				adj+=1
				if a[i]==b[i]:
					adjcount+=1

		
			elif "PSP" in a[i]:
				psp+=1
				if a[i]==b[i]:
					pspcount+=1

			elif "RB" in a[i]:
				adv+=1
				if a[i]==b[i]:
					advcount+=1

			if "PRP" in a[i]:
				prp+=1
				if a[i]==b[i]:
					prpcount+=1


			elif "VM" in a[i] or "VAUX" in a[i]:
				verb+=1
				if a[i]==b[i]:
					vcount+=1

			if "CC" in a[i]:
				conjunct+=1
				if a[i]==b[i]:
					cccount+=1
print " noun =%s " %(ncount/float(noun))

print " adjective = %s" %(adjcount/float(adj))

print " pronoun = %s" %(prpcount/float(prp))
print " adverb = %s" %(advcount/float(adv))
print " postposition = %s" %(pspcount/float(psp))
print " conjunct = %s" %(cccount/float(conjunct))

'''
def parse(a,z):
	for i in a:
		if i != '\n':
			if "NN" in i.split()[4]:
				name="nounin.txt"
				if z==1:
					name="nounout.txt"
				f=open(name, "a")	
				f.write(i)

			elif "PRP" in i.split()[4]:
			
				name="pronounin.txt"
				if z==1:
					name="pronounout.txt"
				f=open(name, "a")
				f.write(i)
			elif "JJ" in i.split()[4]:

				name="adjectivein.txt"
				if z==1:
					name="adjectiveout.txt"
				f=open(name, "a")
				f.write(i)
			elif "VM" in i.split()[4] or "VAUX" in i.split()[4]:

				name="verbin.txt"
				if z==1:
					name="verbout.txt"
				f=open(name, "a")
				f.write(i)
			elif "CC" in i.split()[4]:

				name="conjunctionin.txt"
				if z==1:
					name="conjunctionout.txt"
				f=open(name, "a")
				f.write(i)
			elif "RB" in i.split()[4]:

				name="adverbin.txt"
				if z==1:
					name="adverbout.txt"
				f=open(name, "a")
				f.write(i)
			elif "PSP" in i.split()[4]:
			
				name="postpositionin.txt"
				if z==1:
					name="postpositionout.txt"
				f=open(name, "a")
				f.write(i)

'''	
