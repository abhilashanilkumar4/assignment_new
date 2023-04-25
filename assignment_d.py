def find_duplicates(A):
    n = len(A)
    duplicates = []

    B = {}
    for num in A:
        B[num] = B.get(num, 0) + 1


    for num, count in B.items():
        if count > 1:
            duplicates.append(num)

    return duplicates

A = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9]
print(find_duplicates(A))
