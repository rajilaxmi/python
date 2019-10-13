# to find the largest element from the list
list1=[23,67,34,9,46]
max=list1[0]
for l in list1:
	if max<l:
		max=l
print list1
print "largest element in the list: %d"%max