from functools import reduce

#The approach that allows division.
def exclusive_product(arr):
    product = reduce((lambda x,y: x*y), arr) #Needlessly fancy way to get product.
    result = []
    for a in arr:
        result.append(product/a)
    return result

print(exclusive_product([1, 2, 3, 4, 5]))


#The approach that allows no division
def no_division(arr):
    return branch(arr, 0, 1)

#Function that keeps a subproduct to reduce redundant multiplications.
def branch(arr, idx, subproduct):
    #Terminates recursion
    if idx == len(arr)-1:
        return [subproduct]

    product = subproduct
    for a in arr[idx+1:]:
        product *= a

    #Recursive step
    return [product] + branch(arr,idx+1, subproduct*arr[idx])

print(no_division([1, 2, 3, 4, 5]))
