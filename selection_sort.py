lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j

        if min_idx != i:
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


print(selection_sort(lst))
# Time Complexity: O(n * n)
# Auxiliary Space: O(1)
