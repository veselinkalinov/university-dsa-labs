def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr: list) -> list: ...


if __name__ == "__main__":
    arr = [7, 3, 5, 2]
    arr_sorted = insertion_sort(arr)
    print(arr_sorted)
