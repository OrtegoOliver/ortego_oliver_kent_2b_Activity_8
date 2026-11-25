def merge_k_arrays(arrays):
    min_heap = merge_k_arrays()

    result = []

    for i in range(len(arrays)):
        if len(arrays[i]) > 0:
            min_heap.insert((arrays[i][0], i, 0))

    while min_heap.size() > 0:
        value, array_index, element_index = min_heap.extract()

        result.append(value)

        next_index = element_index + 1

        if next_index < len(arrays[array_index]):
            next_value = arrays[array_index][next_index]

            min_heap.insert((next_value, array_index, next_index))

    return result



arrays = [
    [1, 4, 7],
    [2, 5, 8, 10],
    [3, 6, 9]
]

print("Merged array:", merge_k_arrays(arrays))

print()