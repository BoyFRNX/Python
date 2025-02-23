from bisect import bisect_left


# First Attempt: (iterative function using bisect function)


def binary_search_iterative(array, x, lo=0, hi=None):  # can't use array to specify default for hi
    if hi is None:
        hi = len(array)  # hi defaults to len(array)
    pos = bisect_left(array, x, lo, hi)  # find insertion position
    if pos < hi and array[pos] == x:
        return pos
    else:
        return -1  # don't walk off the end


numbers = list(range(1, 210000000))

print("(Binary Search Iterative) Input the list and number you want to index:")
arr1 = input("List:")
arr = globals()[arr1]
num = int(input("Number:"))
print(f"Index of {num} in {arr1}: {binary_search_iterative(arr, num)}")


# Second Attempt: (recursive function using bisect function)


def binary_search_recursive(array, x, lo=0, hi=None):
    if hi is None:
        hi = len(array)
    pos = bisect_left(array, x, lo, hi)
    while lo < hi:
        if pos != hi and array[pos] == x:
            return pos
    else:
        return -1


print("\n(Binary Search Recursive) Input the list and number you want to index:")
print("Input the list and number you want to index:")
arr1 = input("List:")
arr = globals()[arr1]
num = int(input("Number:"))
print(f"Index of {num} in {arr1}: {binary_search_iterative(arr, num)}")
