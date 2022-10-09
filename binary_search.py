lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # In Binary Search list must be sorted


def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if target == lst[mid]:
            return mid
        elif target > lst[mid]:
            left = mid
        else:
            right = mid

    return -1


print(binary_search(lst, 5))
# Time Complexity: O(log n)
# Auxiliary Space: O(1)
