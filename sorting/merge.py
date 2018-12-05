
def merge(left_array, right_array, arr):
    l = 0
    r = 0
    i = 0

    while(l < len(left_array) and r < len(right_array)):
        if (left_array[l] < right_array[r]):
            arr[i] = left_array[l]
            l = l+1

        else:
            arr[i] = right_array[r]
            r = r+1
        i = i+1

    while(l < len(left_array)):
        arr[i] = left_array[l]
        i = i+1
        l = l+1
    
    while(r < len(right_array)):
        arr[i] = right_array[r]
        i = i+1
        r = r+1

def merge_sort(arr):
    print("Splitting ", arr)
    num = len(arr)
    if(num < 2):
        return
    
    mid = int(num/2)
    left_array = arr[:mid]
    right_array = arr[mid:]

    merge_sort(left_array)
    merge_sort(right_array)

    merge(left_array, right_array, arr)


arr = [2,4,7,1,5,9,0,3]
print(arr)
merge_sort(arr) 
print(arr) 