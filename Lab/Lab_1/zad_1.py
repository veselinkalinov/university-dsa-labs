# Даден е едномерен масив. Да се намери броят на двойките съседни елементи, в които сумата на двата елемента е по - малка от 50.

a = [10, 30, 25, 20, 40]


def find_couples(arr: list) -> int:
    count = 0
    for i in range(0, len(arr) - 1):
        sum = arr[i] + arr[i + 1]
        if sum < 50:
            count += 1
    return count


count_found = find_couples(a)
print(count_found)
