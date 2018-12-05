
def bubble_sort(arr):
    for pos in range(len(arr)-1, 0, -1):
        swap_flag = False # takes best case to O(n)
        for i in range(pos):
            print(".", end=" ") # to see the inner workings of the algorithm
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_flag = True
        print(" ")
        if not swap_flag:
            break

arr = [2,4,7,1,5,9,0,3]
# arr = [0, 1, 2, 3, 4, 5, 7, 9]
print(arr)
bubble_sort(arr) 
print(arr)     