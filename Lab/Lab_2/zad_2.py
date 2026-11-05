# 1. Да се състави рекурсивна функция, която преобразува цяло десетично положително число в двуично
# 2. Да се намери сумата на елементи на едномерен масив, чрез рекурсивна функция

import random


def decimal_to_binary(n: int) -> str:
    if n < 2:
        return str(n)

    return decimal_to_binary(n // 2) + str(n % 2)


def array_sum(arr: list, n: int) -> int:
    if n == 0:
        return 0

    return arr[n - 1] + array_sum(arr, n - 1)


if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    print(decimal_to_binary(n))
    print()

    arr = [random.randint(1, 100) for i in range(random.randint(1, 50))]
    print(arr)
    print()
    print(f"Sum: {array_sum(arr, len(arr))}")
