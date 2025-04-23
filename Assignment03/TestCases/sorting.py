import os
import csv
import argparse

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

    for weight, i in value_per_weight:
        if weights[i] <= capacity:
            total_value += values[i]
            capacity -= weights[i]
        else:
            total_value += values[i] * (capacity / weights[i])
            break
    
    return total_value


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
    
def top_down(coins, amount):
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
            # solves 8.csv causing infinite recursion
            if C==0:
                continue
            result = F(S - C)
            if result >= 0 and result < minNumberCoin:
                minNumberCoin = 1 + result

        memo[S] = -1 if minNumberCoin == float('inf') else minNumberCoin
        return memo[S]

    return F(amount)

def knapsack(values, weights, capacity):
    n = len(values)
    
    # Initialize memo table with zeros
    memo = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the memo table bottom-up
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] > w:
                memo[i][w] = memo[i - 1][w]
            else:
                memo[i][w] = max(memo[i - 1][w], memo[i - 1][w - weights[i - 1]] + values[i - 1])

    return memo[n][capacity]

def print_result(result):
    if result % 1 == 0:
        print("{:.0f}".format(result))
    else:
        print("{:.4f}".format(result))


def main(problem=None, args=None):
    # Get what porblem the user wants to solve
    problem = problem.strip() if problem else None
    if problem is None:
        problem = input("Which problem do you want to solve? (1:Greedy, 2:maxSubSum, 3:TopDown, 4:Knapsack, 5:RUN ALL PROBLEMS): ").strip()
    folder_path = ""
    output_path = ""

    if problem not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
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

    elif(problem == '5'):
        print("Running all problems...")
        print("Problem 1")
        main('1')
        print("------------------------------------------------------------------------------")
        print("Problem 2")
        main('2')
        print("------------------------------------------------------------------------------")
        print("Problem 3")
        main('3')
        print("------------------------------------------------------------------------------")
        print("Problem 4")
        main('4')
        
        return

        

    if args and args.file:
        # Use single file override
        file_list = [args.file]
    else:
        # Use all .csv files in the folder
        file_list = [
            os.path.join(folder_path, f)
            for f in os.listdir(folder_path)
            if f.lower().endswith('.csv')
        ]

    for file_path in file_list:
        filename = os.path.basename(file_path)
        print(f"\nProcessing file: {filename}")
        
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = [row for row in reader]
        
        try:
            # if args and args.output:
            #     valid_output_path = args.output
            # else:
            #     
            valid_output_path = os.path.join(output_path, filename[:-4] + ".txt")

            with open(valid_output_path, newline='') as csvfile:
                reader2 = csv.reader(csvfile)
                valid_result = next(reader2)[0]

            

            if problem == '1':
                value = list(map(int, data[0]))
                weight = list(map(int, data[1]))
                capacity = int(data[2][0])
                result = greedy(value, weight, capacity)
                print_result(result)
                #print(f"Valid Output: {valid_result}")

            elif problem == '2':
                numbers = list(map(int, data[0]))
                result = max_subarray_sum(numbers, 0, len(numbers) - 1)
                print_result(result)
                #print(f"Valid Output: {valid_result}")

            elif problem == '3':
                target = int(data[0][0])
                coins = list(map(int, data[1]))
                result = top_down(coins, target)
                print_result(result)
                #print(f"Valid Output: {valid_result}")

            elif problem == '4':
                value = list(map(int, data[0]))
                weight = list(map(int, data[1]))
                capacity = int(data[2][0])
                result = knapsack(value, weight, capacity)
                print_result(result)
                #print(f"Valid Output: {valid_result}")


        except Exception as e:
            print(f"Error processing {filename}: {e}")
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run sorting algorithms on CSV files.")
    parser.add_argument("-p", "--problem", help="Problem number to run (1-5)")
    parser.add_argument("-f", "--file", help="Path to the CSV file")
    parser.add_argument("-o", "--output", help="Path to the output file")
    args = parser.parse_args()

    
    main(args.problem, args)