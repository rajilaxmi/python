''' count the number of strings where the string length 
is 2 or more and the first and last character are same 
from a given list of strings. '''
list1=['abc','aba','1221']
count=0
for l in list1:
	if len(l)>1 and l[0]==l[-1]:
		count+=1
print "the number of strings with first and last character same is: %d"%count
