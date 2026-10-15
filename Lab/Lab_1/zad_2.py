# Даден е едномерен масив, да се състави вотри едномерен масив със следните елементи: Първи елемент - произведението на най - малкия и най - големия елемент на първия масив, Втори елемент - средно аритметичната стойност на сумата на четните елементи на първия масив, Трети елемент - броя на нечетните елементи на първия масив, Четвърти елемент - броят на елементите, чиято стойност е по - голяма от индексите на двата съседни елемента на съответният елемент.

A = [10, 30, 25, 20, 40]
B = []


def min_max_prod(arr: list) -> int:
    min_value = arr[0]
    max_value = arr[0]

    for i in range(0, len(arr) - 1):
        if min_value > arr[i + 1]:
            min_value = arr[i + 1]
        if max_value < arr[i + 1]:
            max_value = arr[i + 1]

    prod = min_value * max_value

    return prod


def avg(arr: list) -> float:
    sum = 0
    count = 0
    avg = 0
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            sum += arr[i]
            count += 1

    avg = round(sum / count, 2)
    return avg


def odds(arr: list) -> int:
    count = 0
    for i in range(0, len(arr)):
        if arr[i] % 2 != 0:
            count += 1

    return count


def val_idx(arr: list) -> int:
    count = 0
    for i in range(1, len(arr) - 1):
        if arr[i] > i - 1 and arr[i] > i + 1:
            count += 1
    return count


el_1 = min_max_prod(A)
el_2 = avg(A)
el_3 = odds(A)
el_4 = val_idx(A)
B = [el_1, el_2, el_3, el_4]
print(B)
