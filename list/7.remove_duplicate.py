# to remove all the duplicate values from the list
list1=[1,4,2,4,5,1,2,5]
list2=[]
for l in list1:
	if l not in list2:
		list2.append(l)
print "List without duplicate values:",list2