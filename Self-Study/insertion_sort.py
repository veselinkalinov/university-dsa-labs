def insertion_sort(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key


if __name__ == "__main__":
    arr = [6, 2, 5, 1]

    arr_sorted = insertion_sort(arr)
    print(arr_sorted)
