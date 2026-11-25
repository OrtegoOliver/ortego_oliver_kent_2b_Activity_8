def kth_largest(numbers, k):
    if k <= 0 or k > len(numbers):
        return None

    min_heap = kth_largest()

    for number in numbers:
        min_heap.insert(number)

        if min_heap.size() > k:
            min_heap.extract()

    return min_heap.peek()



values = [3, 2, 1, 5, 6, 4]
k = 2

print("Numbers:", values)
print("K:", k)
print("Kth largest:", kth_largest(values, k))
print("Check using sorting:", sorted(values, reverse=True)[k - 1])

print()