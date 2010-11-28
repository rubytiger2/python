#example of using the break statement.
for x in range(10):
	print x	
	if x==5:
		break

#example of using the continue statement
#see how it skips printing of 5	
for x in range(10):	
	if x==5:
		continue
	print x
