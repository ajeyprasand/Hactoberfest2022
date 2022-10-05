def binary_search(arr, low, high, x):

    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
         elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return -1
    
arr = [ 2, 3, 4, 10, 40 ] 
x = 10 #X is the element which is to be checked if present in the array or not
index = binary_search(arr, 0, len(arr)-1, x)
if index != -1:
    print("Element is present at index", index)
else:
    print("Element is not present in array")
 
