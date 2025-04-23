import csv
import argparse

def cross(arr, left, mid, right):
    # left
    left_sum = float('-inf')
    total = 0
    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)

    # right
    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_sum = max(right_sum, total)

    return left_sum + right_sum

def max_subarray_sum(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2
    left_max = max_subarray_sum(arr, left, mid)
    right_max = max_subarray_sum(arr, mid + 1, right)
    cross_max = cross(arr, left, mid, right)

    return max(left_max, right_max, cross_max)
    return total_value

def print_result(result):
    if result % 1 == 0:
        print("{:.0f}".format(result))
    else:
        print("{:.4f}".format(result).rstrip('0'))

def main(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    numbers = list(map(int, data[0]))
    result = max_subarray_sum(numbers, 0, len(numbers) - 1)
    
    print_result(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run knapsack algorithm on a single CSV file.")
    parser.add_argument("file", help="Path to the CSV file")
    args = parser.parse_args()
    main(args.file)
