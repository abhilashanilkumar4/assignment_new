def kth_largest_smallest(A, k):

    smallest = sorted(A)[k-1]
    largest = sorted(A, reverse=True)[k-1]

    return largest, smallest


A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(kth_largest_smallest(A, k))
