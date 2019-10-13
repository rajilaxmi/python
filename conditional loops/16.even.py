# print the even numbers b/w 100 and 400(both included) with comma separation
even=[]
for l in range(100,401):
	if l%2==0:
		even.append(str(l))
print(",".join(even))
