#Create a list
a = ['cat','window','defenestarte']

#get the number of elements in the list
len(a)

#inserting an element in the front of the list.
a.insert(0,"cool")

#make a slice copy of an entire list
a[:]
	1. Can assign it some where
	b = a[:]

	2. would be used in a for loop if we need to modify the list we are iterating over
	for x in a[:]:
		if len(x) > 6: a.insert(0,x)