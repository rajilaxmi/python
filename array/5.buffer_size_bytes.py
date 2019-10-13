# to print the buffer info and the length of the arrray and also the size of the memory buffer in bytes
from array import *
a=array('i',[1,3,5,7,9])
for i in a:
	print i
print "the buffer info :"+str(a.buffer_info())
print "the size of the memory buffer:"+str(a.buffer_info()[1]*a.itemsize)
