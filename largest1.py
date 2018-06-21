def large(a, b):
	ab=str(a)+str(b)
	ba=str(b)+str(a)
	return cmp(int(ba), int(ab))
a = [5,6,7,8,9]
sorted_array=sorted(a, cmp=large)
num= "".join([str(i) for i in sorted_array])
print(num)
