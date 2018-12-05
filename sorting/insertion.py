
def insertion(arr):
    for pos in range(1, len(arr)):
        # start with 1 cause we assume the first elem is sorted
        hole = pos
        value = arr[pos]

        while(hole > 0 and arr[hole-1] > value):
            arr[hole] = arr[hole-1]
            hole = hole-1
        
        arr[hole] = value

arr = [2,4,7,1,5,9,0,3]
print(arr)
insertion(arr) 
print(arr)   

