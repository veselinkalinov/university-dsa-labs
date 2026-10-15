# Площадка представлява два или повече еднакви съседни елемента
# в едномерен масив. Да се намерят броят на площадките
# и дължината на всяка от тях.

A = [2, 2, 2, 7, 4, 4, 5, 5, 5, 5, 1, 1]


def find_plateaus(arr: list) -> tuple[int, list[int]]:
    count = 0
    current_length = 1
    lengths = []

    if len(arr) == 0:
        return 0, []

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            current_length += 1
        else:
            if current_length >= 2:
                count += 1
                lengths.append(current_length)
            current_length = 1

    if current_length >= 2:
        count += 1
        lengths.append(current_length)

    return count, lengths


count_found, plateau_lengths = find_plateaus(A)

print("Брой площадки:", count_found)
print("Дължини на площадките:", plateau_lengths)
