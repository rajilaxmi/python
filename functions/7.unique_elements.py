# to print the unique elements in a list
def unique(list1):
	uni=[]
	for l in list1:
		if l not in uni:
			uni.append(l)
	return uni
	

list1=[1,1,1,2,2,3,3,3,3,4,4,5,5,5]
print unique(list1)


'''
[1,2,3,4,5]
'''
