#to append items from inerrable to the end of the array
from array import *
a=array('i',[1,3,5,7,9])
a.extend(a)
for i in a:
	print i