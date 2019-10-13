# to find the difference between two lists
list1=[1,3,5,7]
list2=[2,4,6,8]
list3=[]
for x in list1:
	for y in list2:
		list3.append(y-x)
print list3