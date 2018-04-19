n = int(input("nhap day so:"))
arr = []
for i in xrange(0,n):
	
	arr.append(i+1)
print (arr)
sum = 0
for i in xrange(0,n):
	if(arr[i] % 2 == 0):
		sum = sum +arr[i]
print "tong so chan: ", sum

	