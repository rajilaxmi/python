# Insertion Sort
def insertion(arr):
	for i in range(1,len(arr)):
		key=arr[i]
		j=i-1
		while(j>=0 and arr[j]>key):
			arr[j+1]=arr[j]
			j=j-1
		arr[j+1]=key
		

#Main
arr = [12,11,13,5,6]
insertion(arr)
for i in range(len(arr)):
	print("%d "%arr[i])
