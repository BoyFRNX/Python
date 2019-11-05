from bisect import bisect_left


# First Attempt: (iterative function)


def binary_search_iterative(array, x, lo=0, hi=None):  # can't use a to specify default for hi
    if hi is None:
        hi = len(array)  # hi defaults to len(a)
    pos = bisect_left(array, x, lo, hi)  # find insertion position
    if pos < hi and array[pos] == x:
        return pos
    else:
        return -1  # don't walk off the end


numbers = list(range(1, 11))
print("Input the list and number you want to index:")
print("List:")
arr = input()
print("Number:")
num = int(input())
print(f"Index of {num} in {arr}: {binary_search_iterative(numbers, num)}")


# Second Attempt: (recursive function)


def binary_search_recursive(array, x, lo=0, hi=None):
    if hi is None:
        hi = len(array)
    pos = bisect_left(array, x, lo, hi)
    while lo < hi:
        if pos != hi and array[pos] == x:
            return pos
    else:
        return -1


print("Input the list and number you want to index:")
print("List:")
arr = input()
print("Number:")
num = int(input())
print(f"Index of {num} in {arr}: {binary_search_iterative(numbers, num)}")
