#Bubble Sort
def bubble(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0,n-1):
			if arr[j]>arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

#main
arr=[5,4,3,2,1]
bubble(arr)
for i in range(len(arr)):
	print("%d "%arr[i])

