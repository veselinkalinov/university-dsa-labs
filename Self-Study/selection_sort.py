def selection_sort(arr: list) -> list:
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == "__main__":
    arr = [8, 7, 6, 5, 3, 2, 1, 4, 9]

    sorted_arr = selection_sort(arr)
    print(sorted_arr)
