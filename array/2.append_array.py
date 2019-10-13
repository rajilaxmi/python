# append a new element into an existing array
from array import *
a=array('i',[1,3,5])
print "Original array: "
for i in a:
	print i
a.append(7)
print "New array: "
for i in a:
	print i
	
'''
original array:
1
3
5
New array:
1
3
5
7
'''


