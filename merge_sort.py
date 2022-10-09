lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def merge_sort(lst):
    if len(lst) > 1:

        # Finding the mid of the array
        mid = len(lst) // 2

        # Dividing the array elements
        left = lst[:mid]

        # into 2 halves
        right = lst[mid:]

        # Sorting the first half
        merge_sort(left)

        # Sorting the second half
        merge_sort(right)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    return lst


print(merge_sort(lst))
# Time Complexity: O(n * log n)
# Auxiliary Space: O(n)
