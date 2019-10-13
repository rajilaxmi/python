def binary(arr, l, r, x):
	if r>=l:
		mid=(l+r)/2
		if arr[mid]==x:
			return mid
		elif arr[mid]>x:
			return binary(arr,l,mid-1,x)
		else:
			return binary(arr,mid+1,r,x)
	else:
		return -1

	

arr=[12,36,45,51,60,78,82,96,108]
x=25
result = binary(arr,0,len(arr)-1,x)
if result != -1:
	print "Found element at index %d"%result
else:
	print "Couldnt find the element"
