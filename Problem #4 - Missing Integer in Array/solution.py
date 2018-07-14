
#Finds lowest positive integer missing from array.
def lowest_positive_missing(arr):
    #Swap every positive integer a to the ath position (a-1, due to 0-indexing).
    for round in range(0,2):
        for idx, a in enumerate(arr):
            if a > 0 and a < len(arr):
                swap(arr,idx,a-1)

    print(arr)
    #Now we can check if a positive integer exists by ascertaining whether a is
    #at position a-1. If not, then that is the next missing positive integer.
    check = 1
    for a in arr:
        if a != check:
            return check
        else:
            check += 1
    return check

def swap(arr, i ,j):
    arr[i], arr[j] = arr[j], arr[i]


print(lowest_positive_missing([3, 4, -1, 1])) #Should be 2
print(lowest_positive_missing([1, 2, 0])) #Should be 3
print(lowest_positive_missing([1, 3, 4,3,1,1,-2,1,2,4,7,6,5,8,9,1000,10])) #Should be 11
