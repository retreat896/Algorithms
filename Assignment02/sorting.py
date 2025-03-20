import sys

#print the array like gradescope wants it
def arrayToString(arr):
    return ",".join(str(x) for x in arr)


# Output the whole array after each element is placed
def insertionSort(arr):
    i, j, key = 0, 0, 0
    print(arrayToString(arr))
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key
        print(arrayToString(arr))
    return arrayToString(arr)  # return the sorted array to appease the gradescope gods


# Output the whole array after each swap occurs
def selectionSort(arr):
    print(arrayToString(arr))
    for i in range(len(arr)):
        smallesti = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallesti]:
                smallesti = j
        if smallesti != i:
            # swap
            arr[smallesti], arr[i] = arr[i], arr[smallesti]
            print(arrayToString(arr))
    return arrayToString(arr)  # still return the sorted array for gradescope happiness

#pivot 
def partition(arr, start, end):
    pivot = arr[end]
    left = start - 1

    for i in range(start, end):
        if arr[i] <= pivot:
            left += 1
            # swap here
            arr[left], arr[i] = arr[i], arr[left]
            print(arrayToString(arr))

    arr[left + 1], arr[end] = arr[end], arr[left + 1]
    print(arrayToString(arr))
    return left + 1


# Output the whole array after each swap occurs
# Output the whole array after each pivot is placed
# Always choose the first element of the sub-array as the pivot element.
# WILL WORK IN GRADESCOPE
def quickSortGS(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSortGS(arr, low, pivot - 1)
        quickSortGS(arr, pivot + 1, high)
        
    return arrayToString(arr)


# Output the whole array after each swap occurs
# Output the whole array after each pivot is placed
# Always choose the first element of the sub-array as the pivot element.
# HOARE's partition Method
# WILL NOT WORK IN GRADESCOPE
def quickSort(arr):

    return False


def merge(arr, left, middle, right):
    leftSize = middle - left + 1
    rightSize = right - middle
    leftArr = []
    rightArr = []

    for i in range(leftSize):
        leftArr.append(arr[left + i])
    for i in range(rightSize):
        rightArr.append(arr[middle + 1 + i])

    leftI = 0
    rightI = 0
    valueI = left

    while leftI < leftSize and rightI < rightSize:
        if leftArr[leftI] <= rightArr[rightI]:
            arr[valueI] = leftArr[leftI]
            leftI += 1
        else:
            arr[valueI] = rightArr[rightI]
            rightI += 1
        valueI += 1

    while leftI < leftSize:
        arr[valueI] = leftArr[leftI]
        leftI += 1
        valueI += 1

    while rightI < rightSize:
        arr[valueI] = rightArr[rightI]
        rightI += 1
        valueI += 1

    # might need to delete arrays here but this is not C++
    return arr


# Output the whole array after each merge function is called
# The left half of the sub-array will contain any extra elements for non-even splits.
def mergeSortRecursive(arr, left, right, isRecursiveCall=True):
    if left < right:
        middle = left + (right - left) // 2

        mergeSortRecursive(arr, left, middle, True)
        mergeSortRecursive(arr, middle + 1, right, True)

        # merge here
        arr = merge(arr, left, middle, right)
        print(arrayToString(arr))

    return arrayToString(arr)


# CHALLENGE PROBLEM
# Implement Merge Sort iteratively.
# Output the whole array after each merge function is called
# The left half of the sub-array will contain any extra elements for non-even splits.
def mergeSortIterative(arr):
    size = 1
    while size <= len(arr)-1:
        left = 0
        while left < len(arr)-1:
            mid = min(left + size-1, len(arr)-1)
            right = min(left + 2 * size-1, len(arr)-1)
            merge(arr, left, mid, right)
            print(arrayToString(arr))
            left += 2 * size
        size = 2 * size

    print(arrayToString(arr))        
    return arrayToString(arr)
    return False


if __name__ == "__main__":
    # First Argument from args is file to read the array from
    if len(sys.argv) != 3:
        print("Usage: python main.py <input array file path> <algorithm number>")
        print("Algorithms:")
        print("1. Insertion Sort")
        print("2. Selection Sort")
        print("3. Quick Sort")
        print("4. Merge Sort Recursive")
        print("5. CHALLENGE PROBLEM: Merge Sort Iterative")
        sys.exit(1)
    with open(sys.argv[1], "r") as f:
        arr = [int(x) for x in f.read().split(",")]

    # Second Argument from args is the sorting algorithm to use
    # 1. Insertion Sort
    # 2. Selection Sort
    # 3. Quick Sort
    # 4. Merge Sort Recursive
    # 5. CHALLENGE PROBLEM: Merge Sort Iterative
    algorithm = int(sys.argv[2])

    if algorithm == 1:
        print(insertionSort(arr) + " ")  # why does gradescope need a space???????
    elif algorithm == 2:
        print(selectionSort(arr) + " ")
    elif algorithm == 3:
        length = len(arr)
        print(quickSortGS(arr, 0, length-1) + " ")
    elif algorithm == 4:
        print(arrayToString(arr))
        print(mergeSortRecursive(arr, 0, len(arr) - 1, False) + " ")
    elif algorithm == 5:
        print(mergeSortIterative(arr))
    elif algorithm == 6:
        print(quickSort(arr) + " ")
