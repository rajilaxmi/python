# print median
list1=[23,56,34,78,12,90,65,43]
median=0
count=0
list1.sort()
for l in list1:
	count+=1
mid=count/2
median=list1[mid]
print list1
print "The median is %d"%median