#for statment
#pythons for statement iterates over the items of any sequence (list or string) in the order that they appear in the sequence

a = ['cat','window','defenestrate']

for x in a:
	print x, len(x)

# A splice list is used in a for loop if we need to modify the list we are iterating over
#	for x in a[:]:
#		if len(x) > 6: a.insert(0,x)

# another example
a = [1,2,3]
for x in a[:]:
	if x==2:
		a.insert(3,4)


#to iterate over the indices of a sequence you can combine range() and len() as follows:
a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
	print i, a[i]