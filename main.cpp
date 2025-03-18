
#include <iostream>
#include <iomanip>
    using namespace std;
void printArray(int values[], int size)
{
    bool addComma = false;
    for (int i = 0; i < size; i++)
    {
        if (addComma)
        {
            cout << ",";
        }
        cout << values[i];
        addComma = true;
    }
    cout << endl;
    // cin.ignore();
}
void addRandomValues(int values[], int size)
{
    for (int i = 0; i < size; i++)
    {
        values[i] = rand() % 100;
    }
}
void merge(int values[], int left, int mid, int right)
{
    // Create temporary arrays
    int sizeLeft = mid - left + 1;
    int sizeRight = right - mid;
    int *leftArray = new int[sizeLeft];
    int *rightArray = new int[sizeRight];
    // Copy data into temporary arrays
    for (int i = 0; i < sizeLeft; i++)
    {
        leftArray[i] = values[left + i];
    }
    for (int i = 0; i < sizeRight; i++)
    {
        rightArray[i] = values[mid + 1 + i];
    }
    int leftIndex = 0;
    int rightIndex = 0;
    int valuesIndex = left;
    // zipper merge the arrays
    while (leftIndex < sizeLeft && rightIndex < sizeRight)
    {
        if (leftArray[leftIndex] <= rightArray[rightIndex])
        {
            values[valuesIndex] = leftArray[leftIndex];
            leftIndex++;
        }
        else
        {
            values[valuesIndex] = rightArray[rightIndex];
            rightIndex++;
        }
        valuesIndex++;
    }
    // if anything is on the left, merge it in
    while (leftIndex < sizeLeft)
    {
        values[valuesIndex] = leftArray[leftIndex];
        leftIndex++;
        valuesIndex++;
    }
    // if anything is on the right, merge it in
    while (rightIndex < sizeRight)
    {
        values[valuesIndex] = rightArray[rightIndex];
        rightIndex++;
        valuesIndex++;
    }
    delete[] leftArray;
    delete[] rightArray;
}
void mergeSort(int values[], int left, int right, int size)
{
    if (left < right)
    {
        int mid = left + (right - left) / 2;
        mergeSort(values, left, mid, size);
        mergeSort(values, mid + 1, right, size);
        merge(values, left, mid, right);
        printArray(values, size);
    }
}
void selectionSort(int values[], int size)
{
    for (int i = 0; i < size; i++)
    {
        int smallestIndex = i;
        for (int j = i + 1; j < size; j++)
        {
            if (values[j] < values[smallestIndex])
            {
                smallestIndex = j;
            }
        }
        if (smallestIndex != i)
        {
            swap(values[i], values[smallestIndex]);
        }
        printArray(values, size);
    }
}
void insertionSort(int values[], int size)
{
    int i, key, j;
    for (i = 1; i < size; i++)
    {
        key = values[i];
        j = i - 1;
        // Move elements of values[0..i-1],
        // that are greater than key, to one
        // position ahead of their current position
        while (j >= 0 && values[j] > key)
        {
            values[j + 1] = values[j];
            j = j - 1;
        }
        values[j + 1] = key;
        printArray(values, size);
    }
}
int partition(int values[], int minPosition, int maxPostition, int arraySize)
{
    int pivot = values[minPosition];
    int openPosition = minPosition;
    int positionLeft = minPosition;
    int positionRight = maxPostition;
    while (positionRight >= positionLeft)
    {
        while (positionRight >= minPosition && values[positionRight] >= pivot)
        {
            positionRight--;
        }
        if (positionRight > minPosition)
        {
            values[openPosition] = values[positionRight];
            openPosition = positionRight;
            printArray(values, arraySize);
            positionRight--;
        }
        while (positionLeft <= maxPostition && values[positionLeft] <= pivot)
        {
            positionLeft++;
        }
        if (positionLeft <= positionRight)
        {
            values[openPosition] = values[positionLeft];
            openPosition = positionLeft;
            printArray(values, arraySize);
            positionLeft++;
        }
    }
    values[openPosition] = pivot;
    printArray(values, arraySize);
    return openPosition;
}
int h_partition(int values[], int start, int end, int arraySize)
{
    int pivot = values[start];
    int left = start - 1;
    int right = end + 1;
    while (true)
    {
        do
        {
            left++;
        } while (values[left] < pivot);
        do
        {
            right--;
        } while (values[right] > pivot);
        if (left >= right)
        {
            return right;
        }
        swap(values[left], values[right]);
        printArray(values, arraySize);
    }
}
void quickSort(int values[], int low, int high, int arraySize)
{
    cout << "quickSort low " << low << " high " << high << endl;
    if (low < high)
    {
        int part = h_partition(values, low, high, arraySize);
        quickSort(values, low, part, arraySize);
        quickSort(values, part + 1, high, arraySize);
    }
}
int main()
{
    srand(time(nullptr));
    const int ARRAY_SIZE = 7;
    int values[ARRAY_SIZE] = {2, 8, 5, 1, 3, 4, 6};
    // int values[ARRAY_SIZE] = { 1, 7, 2, 6, 3, 5, 4 };
    // addRandomValues(values, ARRAY_SIZE);
    printArray(values, ARRAY_SIZE);
    cout << endl
        << endl;
    // selectionSort(values, ARRAY_SIZE);
    // insertionSort(values, ARRAY_SIZE);
    // mergeSort(values, 0, ARRAY_SIZE - 1, ARRAY_SIZE);
    quickSort(values, 0, ARRAY_SIZE - 1, ARRAY_SIZE);
    // printArray(values, ARRAY_SIZE);
    cout << endl;
}
