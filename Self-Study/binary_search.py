def binary_search(arr: list, target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
            continue
        elif arr[mid] < target:
            left = mid + 1
            continue
    return -1


if __name__ == "__main__":
    arr = [9, 4, 12, 7, 2]
    arr.sort()
    print(binary_search(arr, 7))
    print(binary_search([3, 6, 9], 4))
