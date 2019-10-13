# to remove an element from an array
from array import *
a=array('i',[1,3,5,7])
for i in a:
	print i
a.pop(3)
print "After removing an element:" 
for i in a:
	print i

'''
1
3
5
7
After removing an element:
1
3
5
'''