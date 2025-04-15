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


def greedy():

    return


def main():
    # Get what porblem the user wants to solve
    problem = input("Which problem do you want to solve? (1:Greedy, 2:maxSubSum, 3:TopDown, 4:Knapsack): ").strip()
    folder_path = ""

    if problem not in ['1', '2', '3', '4']:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        return
    
    if(problem == '1'):
        folder_path = "./TestCases/Problem1/input_files/"

    elif(problem == '2'):
        folder_path = "./TestCases/Problem2/input_files/"

    elif(problem == '3'):
        folder_path = "./TestCases/Problem3/input_files/"

    elif(problem == '4'):
        folder_path = "./TestCases/Problem4/input_files/"

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
                if(problem == '1'):
                    # Line 1: value
                    # Line 2: weight
                    # Line 3: capacity
                    greedy()
                elif(problem == '2'):
                    # Line 1: array of numbers
                    greedy()
                elif(problem == '3'):
                    # Line 1: Target sum
                    # Line 2: Array of coin values
                    greedy()
                elif(problem == '4'):
                    # Line 1: value
                    # Line 2: weight
                    # Line 3: capacity
                    greedy()
                
                greedy()
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    return


if __name__ == "__main__":
    main()

