lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


print(linear_search(lst, 5))
# Time Complexity: O(N)
# Auxiliary Space: O(N)
