# remove the first occurence of a specified element from an array
from array import *
a=array('i',[1,3,5,3,7,3,9])
ele=3
'''
for i in a:
	if ele==i:
		del i 
'''
b=array('i',[])
for i in a:
	if i!=3:
		b.append(i)
print "after removing all the occurence:"
for i in b:
	print i
	
'''
afer removing all the occurence:
1
5
7
9
'''