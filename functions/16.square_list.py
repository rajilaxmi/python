# 16. to display the squares of numbers in a list which has values b/w 1-30 (included)
def square():
	list1=[]
	for l in range(1,31):
		list1.append(l*l)
	print list1
	
square()

'''
[1,4,9,16,......,841,900]
'''
