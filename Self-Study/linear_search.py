def linear_search(arr: list, target: int) -> int:
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


if __name__ == "__main__":
    assert linear_search([9, 4, 12, 7, 2], 7) == 3
    assert linear_search([5, 2, 5, 8], 5) == 0
    assert linear_search([3, 6, 9], 4) == -1
    assert linear_search([], 10) == -1
