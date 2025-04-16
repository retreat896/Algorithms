import os
import csv

def get_csv():
    while True:
        file_path = input("Enter the path to the CSV file: ").strip()
        if os.path.exists(file_path) and file_path.lower().endswith('.csv'):
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                data = [row for row in reader]
            return data
        else:
            print("File not found or not a CSV. Please try again.")


def greedy(values, weights, capacity):
    # Calculate the maximum value of fractional knapsack problem.
    # value: list of n items
    # weight: list of weights of items
    # capacity: maximum weight capacity of the knapsack
    # n: number of items

    n = len(values)
    value_per_weight = []
    for i in range(n):
        value_per_weight.append((values[i] / weights[i], i))
    value_per_weight.sort(reverse=True, key=lambda x: x[0])
    total_value = 0
    fractions = [0] * n

    for weight, i in value_per_weight:
        if weights[i] <= capacity:
            fractions[i] = 1
            total_value += values[i]
            capacity -= weights[i]
        else:
            fractions[i] = capacity / weights[i]
            total_value += values[i] * fractions[i]
            break
    
    return total_value, fractions


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
def coin_change(coins, amount):
    memo = [-1] * (amount + 1)

    def F(S):
        # Base cases
        if S < 0:
            return -1
        if S == 0:
            return 0
        if memo[S] != -1:
            return memo[S]

        minNumberCoin = float('inf')
        for C in coins:
            result = F(S - C)
            if result >= 0 and result < minNumberCoin:
                minNumberCoin = 1 + result

        memo[S] = -1 if minNumberCoin == float('inf') else minNumberCoin
        return memo[S]

    return F(amount)

def knapsack():

    return

def main():
    # Get what porblem the user wants to solve
    problem = input("Which problem do you want to solve? (1:Greedy, 2:maxSubSum, 3:TopDown, 4:Knapsack): ").strip()
    folder_path = ""
    output_path = ""

    if problem not in ['1', '2', '3', '4']:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        return
    
    if(problem == '1'):
        folder_path = "./TestCases/Problem1/input_files/"
        output_path = "./TestCases/Problem1/output/"

    elif(problem == '2'):
        folder_path = "./TestCases/Problem2/input_files/"
        output_path = "./TestCases/Problem2/output/"

    elif(problem == '3'):
        folder_path = "./TestCases/Problem3/input_files/"
        output_path = "./TestCases/Problem3/output/"

    elif(problem == '4'):
        folder_path = "./TestCases/Problem4/input_files/"
        output_path = "./TestCases/Problem4/output/"

    if not os.path.isdir(folder_path):
        print("Folder not found.")
        return

    # Loop through all CSV files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            print(f"\nProcessing file: {filename}")
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                data = [row for row in reader]
            try:
                with open(os.path.join(output_path, filename[:-4]+".txt"), newline='') as csvfile:
                    reader2 = csv.reader(csvfile)
                    data2 = next(reader2)[0]

                if(problem == '1'):
                    # Line 1: value
                    value = list(map(int, data[0]))
                    # Line 2: weight
                    weight = list(map(int, data[1]))
                    # Line 3: capacity
                    capacity = int(data[2][0])

                    total_value, fractions = greedy(value, weight, capacity)
                    print(f"Total value: {total_value}")
                    print(f"Fractions: {fractions}")

                    print(f"Valid Output: {data2}")
                elif(problem == '2'):
                    # Line 1: array of numbers
                    
                    numbers = list(map(int, data[0]))
                    max_subarray_sum_result = max_subarray_sum(numbers, 0, len(numbers) - 1)
                    print(f"Numbers: {max_subarray_sum_result}")
                    print(f"Valid Output: {data2}")
                elif(problem == '3'):
                    # Line 1: Target sum
                    target = int(data[0][0])
                    # Line 2: Array of coin values
                    coins = list(map(int, data[1]))
                    print(f"Valid Output: {data2}")
                    # topDown(coins, target)
                elif(problem == '4'):
                    # Line 1: value
                    value = list(map(int, data[0]))
                    # Line 2: weight
                    weight = list(map(int, data[1]))
                    # Line 3: capacity
                    capacity = int(data[2][0])
                    print(f"Valid Output: {data2}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")
    return


if __name__ == "__main__":
    main()

