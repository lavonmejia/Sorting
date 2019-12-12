# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # Total length of both arrays passed to function
    elements = len( arrA ) + len( arrB )

    # Creating an array with value zero with the length of elements
    merged_arr = [0] * elements

    # Indexes to track current position in the arrays
    index_a = 0
    index_b = 0

    # Loop through once for each position in the merged_arr
    for index in range(elements):
        # If we reached the end of arrA set the value of merged_arr to the number of arrB at index_b and increment index_b
        if index_a == len(arrA):
            merged_arr[index] = arrB[index_b]
            index_b += 1
        # Same as above but for arrB
        elif index_b == len(arrB):
            merged_arr[index] = arrA[index_a]
            index_a += 1
        # If the value at arrA is less than the value at arrB given their indexes, set merged_arr at index to the value at arrA
        elif arrA[index_a] < arrB[index_b]:
            merged_arr[index] = arrA[index_a]
            index_a += 1
        # Otherwise set merged_arr at index to the value at arrB
        else:
            merged_arr[index] = arrB[index_b]
            index_b += 1
        # Move to the next position in merged_arr
        index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # If length of the  array to be sorted is less or equal to one, it is already sorted so return it
    if len(arr) <= 1:
        return arr
    # Split the array into two halfs. 
    else:
        midpoint = len(arr) // 2
        # Array of values up to the midpoint. Does not include midpoint.
        L = arr[:midpoint]
        # Array of values from the midpoint to the end
        R = arr[midpoint:]
        # Combine the two sorted halfs of the array, caling merge_sort recursively until the arrays are of length 1
        return(merge(merge_sort(L), merge_sort(R)))
   
    return arr



 




# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


