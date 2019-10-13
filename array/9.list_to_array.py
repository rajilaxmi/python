# append the elements of list into an array
from array import *
a=array('i',[])
list1=[1,3,5]
s=len(list1)
for l in range(len(list1)):
	a.append(list1[l])
for i in a:
	print i

'''
1
3
5
'''