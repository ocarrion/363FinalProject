from CSV_sorting import fish_post_objects

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and int(array[high].interactions) >= int(pivot.interactions):
            high = high - 1

        # Opposite process of the one above
        while low <= high and int(array[low].interactions) <= int(pivot.interactions):
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


quick_sort(fish_post_objects, 0, len(fish_post_objects) - 1)
print([fish.index + " : " + fish.interactions for fish in fish_post_objects])
