# insert an element into an existing array
from array import *
a=array('i',[1,2,3,4,6,7])
for i in a:
	print i
a.insert(3,5)
print "After inserting an element:"
for i in a:
	print i

'''
1
2
3
4
6
7
After inserting an element:
1
2
3
4
5
6
7
'''