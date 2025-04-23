import csv
import argparse

def knapsack(values, weights, capacity):
    n = len(values)
    memo = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
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

def main(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    value = list(map(int, data[0]))
    weight = list(map(int, data[1]))
    capacity = int(data[2][0])
    result = knapsack(value, weight, capacity)
    print_result(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run knapsack algorithm on a single CSV file.")
    parser.add_argument("file", help="Path to the CSV file")
    args = parser.parse_args()
    main(args.file)
