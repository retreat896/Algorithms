# Output the whole array after each element is placed
def insertionSort():
    return False


# Output the whole array after each swap occurs
def selectionSort():
    return False


# Output the whole array after each swap occurs
# Output the whole array after each pivot is placed
# Always choose the first element of the sub-array as the pivot element.
# WILL NOT WORK IN GRADESCOPE
def quickSort():
    return False


# Output the whole array after each merge function is called
# The left half of the sub-array will contain any extra elements for non-even splits.
def mergeSortRecursive():
    return False


# CHALLENGE PROBLEM
# Implement Merge Sort iteratively.
# Output the whole array after each merge function is called
# The left half of the sub-array will contain any extra elements for non-even splits.
def mergeSortIterative():
    return False


if __name__ == "__main__":
    testCase1 = (
        "6,1,20,3,3,4,3,14,13,20,6,8,8,12,13,15,5,18" + "\n"
        "1,6,20,3,3,4,3,14,13,20,6,8,8,12,13,15,5,18" + "\n"
        "1,6,20,3,3,4,3,14,13,20,6,8,8,12,13,15,5,18" + "\n"
        "1,3,6,20,3,4,3,14,13,20,6,8,8,12,13,15,5,18" + "\n"
        "1,3,3,6,20,4,3,14,13,20,6,8,8,12,13,15,5,18" + "\n"
        "1,3,3,4,6,20,3,14,13,20,6,8,8,12,13,15,5,18" + "\n"
        "1,3,3,3,4,6,20,14,13,20,6,8,8,12,13,15,5,18" + "\n"
        "1,3,3,3,4,6,14,20,13,20,6,8,8,12,13,15,5,18" + "\n"
        "1,3,3,3,4,6,13,14,20,20,6,8,8,12,13,15,5,18" + "\n"
        "1,3,3,3,4,6,13,14,20,20,6,8,8,12,13,15,5,18" + "\n"
        "1,3,3,3,4,6,6,13,14,20,20,8,8,12,13,15,5,18" + "\n"
        "1,3,3,3,4,6,6,8,13,14,20,20,8,12,13,15,5,18" + "\n"
        "1,3,3,3,4,6,6,8,8,13,14,20,20,12,13,15,5,18" + "\n"
        "1,3,3,3,4,6,6,8,8,12,13,14,20,20,13,15,5,18" + "\n"
        "1,3,3,3,4,6,6,8,8,12,13,13,14,20,20,15,5,18" + "\n"
        "1,3,3,3,4,6,6,8,8,12,13,13,14,15,20,20,5,18" + "\n"
        "1,3,3,3,4,5,6,6,8,8,12,13,13,14,15,20,20,18" + "\n"
        "1,3,3,3,4,5,6,6,8,8,12,13,13,14,15,18,20,20" + "\n"
        "1,3,3,3,4,5,6,6,8,8,12,13,13,14,15,18,20,20"
    )
    print(testCase1)
