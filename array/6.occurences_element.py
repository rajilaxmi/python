# to get the number of occurences of an element in an array
from array import *
a=array('i',[1,3,5,7,9,5,7,3,5,5,5,5])
e=5
c=0
for i in a:
	if e==a[i]:
		c+=1

print "count of 5: %d"%c