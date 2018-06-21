def repeating (arr,n,k):
for i in range (0,n)
arr[arr[i]%k]+=k
max=arr[0]
result=0
for i in range (1,n)
if arr[i]>max:
max=arr[i]
result=i
arr[i]=arr[i]%k
return result 
arr=[1,2,3,4,2,6,5,3,7,8]
n=len(arr)
k=8
print("enter the unique")
