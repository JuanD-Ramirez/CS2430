# Merge Sort
# The algorithm splits into smaller pieces until each piece has one element
# then merges everything back together in order
def merge_sort(arr):
    comparisons = 0

    #account for a list with 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr, comparisons
    
    #Split the list in half
    middle = len(arr) // 2

    #Recursively sort both halves
    left_half, left_comparisons = merge_sort(arr[:middle])
    right_half, right_comparisons = merge_sort(arr[middle:])

    #Count the comparisons made in the recursive calls
    comparisons += left_comparisons + right_comparisons

    sorted_array = []

    i = j = 0

    #Merge the two halves while counting comparisons
    while i < len(left_half) and j < len(right_half):
        comparisons += 1
        if left_half[i] < right_half[j]:
            sorted_array.append(left_half[i])
            i += 1
        else:
            sorted_array.append(right_half[j])
            j += 1

    #Account for the side that still might have some values
    sorted_array.extend(left_half[i:])
    sorted_array.extend(right_half[j:])

    return sorted_array, comparisons