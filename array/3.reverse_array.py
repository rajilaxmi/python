# print reverse of an array
from array import *
a=array('i',[1,3,5,7])
#for i in range(a):
b=a[::-1]
for i in b:
	print i
b.append(8)
for i in b:
	print i
print type(b)
for i in a:
	print i

'''
7
5
3
1
1
3
5
7
8
<type 'array.array'>
1
3
5
7
'''
