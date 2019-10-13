#6. count the number of even and odd numbers
ecount=0
ocount=0
numbers=[1,2,3,4,5,6,7,8,9,10]
for i in numbers:
	if i%2==0:
		ecount+=1
	else:
		ocount+=1
print ecount, ocount


'''
5 5
'''