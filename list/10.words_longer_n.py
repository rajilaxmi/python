# to find the list of words that are longer than n from a given list of words
list1=["happy","sad","excitement","anger"]
n=4
list2=[]
for l in list1:
	if len(l)>n:
		list2.append(l)

print "words that are longer than n=4 are: ",list2

'''
words that are longer than n=4 are: ['happy','excitement','anger']
'''
