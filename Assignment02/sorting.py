import sys
# Output the whole array after each element is placed
def insertionSort(arr):
    i, j, key = 0, 0, 0
    print(','.join(str(x) for x in arr))
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of values[0..i-1],
        # that are greater than key, to one
        # position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key
        print(','.join(str(x) for x in arr))
    return ','.join(str(x) for x in arr) # return the sorted array to appease the gradescope gods


# Output the whole array after each swap occurs
def selectionSort(arr):
    for ()
    return False


# Output the whole array after each swap occurs
# Output the whole array after each pivot is placed
# Always choose the first element of the sub-array as the pivot element.
# WILL NOT WORK IN GRADESCOPE
def quickSort(arr):
    return False


# Output the whole array after each merge function is called
# The left half of the sub-array will contain any extra elements for non-even splits.
def mergeSortRecursive(arr):
    return False


# CHALLENGE PROBLEM
# Implement Merge Sort iteratively.
# Output the whole array after each merge function is called
# The left half of the sub-array will contain any extra elements for non-even splits.
def mergeSortIterative(arr):
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
    with open(sys.argv[1], 'r') as f:
        arr = [int(x) for x in f.read().split(',')]
    
    # Second Argument from args is the sorting algorithm to use
    # 1. Insertion Sort
    # 2. Selection Sort
    # 3. Quick Sort
    # 4. Merge Sort Recursive
    # 5. CHALLENGE PROBLEM: Merge Sort Iterative
    algorithm = int(sys.argv[2])

    if algorithm == 1:
        print(insertionSort(arr)+" ") # why does gradescope need a space???????
    elif algorithm == 2:
        selectionSort(arr)
    elif algorithm == 3:
        quickSort(arr)
    elif algorithm == 4:    
        mergeSortRecursive(arr)
    elif algorithm == 5:
        mergeSortIterative(arr)

    



