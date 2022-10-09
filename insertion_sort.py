lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def insertion_sort(lst):
    for i in range(1, len(lst)):
        current = lst[i]

        j = i - 1
        while j >= 0 and current < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = current

    return lst


print(insertion_sort(lst))
# Time Complexity: O(n * n)
# Auxiliary Space: O(1)
