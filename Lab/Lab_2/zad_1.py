# **Даден е двумерен масив:**
# 1. Да се създаде едномерен масив, в който да се запишат елементите от двата диагонала на едномерния масив
# 2. Да се намери броят на двойките елементи на едномерния масив, в които и двата елемента са четни числа

import random


def diagonal(matrix: list) -> list:
    arr = []

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(len(matrix)):
        arr.append(matrix[i][i])

    for i in range(min(rows, cols)):
        if i != cols - 1 - i:
            arr.append(matrix[i][cols - 1 - i])

    return arr


def evens(arr: list) -> int:
    count = 0

    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] % 2 == 0 and arr[j] % 2 == 0:
                count += 1

    return count


if __name__ == "__main__":
    twodim_arr = [[random.randint(1, 100) for j in range(4)] for i in range(3)]
    rows = len(twodim_arr)
    cols = len(twodim_arr[0])

    print("Two Dimensional Arra:")
    for i in range(rows):
        for j in range(cols):
            print(twodim_arr[i][j], end=" ")
        print()
    print()

    arr = diagonal(twodim_arr)
    print(f"Array:\n{arr}")
    print("")

    even_links = evens(arr)
    print(f"Even Links: {even_links}")
