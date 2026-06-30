# Quick sort
# Uses the last element as the pivot and partitions the array around it
# smaller on the left and larger on the right

def quick_sort(arr):
    comparisons = 0

    # if the array has 0 or 1 elements, it's already sorted
    if len(arr) <= 1:
        return arr, comparisons

    # Choose the last element as the pivot
    pivot = arr[-1]

    left = []
    right = []

    # Partition the array into left and right based on the pivot
    for i in range(len(arr) - 1):
        comparisons += 1
        
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    # Recursively sort the left and right partitions
    sorted_left, left_comparisons = quick_sort(left)
    sorted_right, right_comparisons = quick_sort(right)

    # Count the comparisons made in the recursive calls
    comparisons += left_comparisons + right_comparisons

    # Combine the sorted left partition, pivot, and sorted right partition
    return sorted_left + [pivot] + sorted_right, comparisons