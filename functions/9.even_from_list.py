# print even numbers from list
def evencount(list1):
	elist=[]
	for l in list1:
		if l%2==0:
			elist.append(l)
	print elist

list1=[25,47,88,24,12,36,47]
evencount(list1)

'''
[88, 24, 12, 36]
'''
