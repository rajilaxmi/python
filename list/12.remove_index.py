# program to print a specified list after removing the 0th, 4th and 5th elements
list1=[1,3,5,7,9,11,13,15]
list2=[]
for i in range(len(list1)):
	if i not in (0,4,5):
		list2.append(list1[i])
print list2