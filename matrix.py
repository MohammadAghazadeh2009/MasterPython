#imports
import numpy as np

#get matrix from user
def get_user_matrix():
    R = 3
    C = 3

    print("Enter values space-separated:")
    vals = list(map(int, input().split()))
    try:
        mat = np.array(vals).reshape(R, C)
        return mat
    except ValueError:
        print("please do not enter to much numbers")
    
#calculate column and row sum
def sum_column(matrix):
    return np.sum(matrix, axis=0)

def sum_row(matrix):
    return np.sum(matrix, axis=1)


matrix = get_user_matrix()
sum_column = list(sum_column(matrix))
sum_row = list(sum_row(matrix))

#main function
def main(row, column):
    print("Row sums:")
    print(f"Row 1: {row[0]}")
    print(f"Row 2: {row[1]}")
    print(f"Row 3: {row[2]}")
    print("/////////////////////")
    print("Column sums:")
    print(f"Column 1: {column[0]}")
    print(f"Column 2: {column[1]}")
    print(f"Column 3: {column[2]}")

#run the project
if __name__ == "__main__":
    main(sum_row, sum_column)
