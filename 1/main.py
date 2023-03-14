import random


def generate_array(n):
    arr = [[random.randint(1, 10) for j in range(n)] for i in range(n)]
    return arr


def read_array_from_file(filename):
    with open(filename, 'r') as file:
        arr = [[int(num) for num in line.split()] for line in file]
    return arr


def write_array_to_file(arr, filename):
    with open(filename, 'w') as file:
        for row in arr:
            for num in row:
                file.write(str(num) + ' ')
            file.write('\n')


def sum_diagonal_elements(arr):
    n = len(arr)
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += arr[i][i]
    return diagonal_sum


def main():
    n = int(input("Enter the size of the array: "))
    option = input(
        "Choose an option: 1. Generate array automatically 2. Read array from file 3. Enter array manually\n")
    if option == '1':
        arr = generate_array(n)
        write_array_to_file(arr, 'array.txt')
    elif option == '2':
        filename = input("Enter the filename: ")
        arr = read_array_from_file(filename)
    elif option == '3':
        arr = [[int(input("Enter element [" + str(i) + "][" + str(j) + "]: ")) for j in range(n)] for i in range(n)]
        write_array_to_file(arr, 'array.txt')
    else:
        print("Invalid option")
        return
    diagonal_sum = sum_diagonal_elements(arr)
    print("The sum of the diagonal elements is", diagonal_sum)


if __name__ == '__main__':
    main()
