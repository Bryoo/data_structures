
def selection(arr):
    for i in range(len(arr)-1):
        imin = i
        for pos in range(i+1, len(arr)):
            if arr[pos] < arr[imin]:
                imin = pos
        arr[imin], arr[i] = arr[i], arr[imin]
arr = [2,4,7,1,5,9,0,3]
print(arr)
selection(arr) 
print(arr)      


