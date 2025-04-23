import csv
import argparse

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

def print_result(result):
    if result % 1 == 0:
        print("{:.0f}".format(result))
    else:
        print("{:.4f}".format(result).rstrip('0'))

def main(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    target = int(data[0][0])
    coins = list(map(int, data[1]))
    result = top_down(coins, target)
    
    print_result(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run knapsack algorithm on a single CSV file.")
    parser.add_argument("file", help="Path to the CSV file")
    args = parser.parse_args()
    main(args.file)
