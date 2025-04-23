import csv
import argparse

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

def print_result(result):
    if result % 1 == 0:
        print("{:.0f}".format(result))
    else:
        print("{:.4f}".format(result).rstrip('0'))

def main(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    value = list(map(int, data[0]))
    weight = list(map(int, data[1]))
    capacity = int(data[2][0])
    result = greedy(value, weight, capacity)

    print_result(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run knapsack algorithm on a single CSV file.")
    parser.add_argument("file", help="Path to the CSV file")
    args = parser.parse_args()
    main(args.file)
