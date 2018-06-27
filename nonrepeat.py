def NonRepeating(arr, n):
 n=5
    for i in range(n):
        j = 0
        while(j < n):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
        if (j == n):
            return arr[i]
     
    return -1
     arr = [1,2,3,1,2]
n = len(arr)
print(NonRepeating(arr, n))
 
