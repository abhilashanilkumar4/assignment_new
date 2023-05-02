def move_negative_elements(MN):
    left = 0
    right = len(MN) - 1
    
    while left <= right:
        while left <= right and MN[left] < 0:
            left += 1
        while left <= right and MN[right] >= 0:
            right -= 1
        
        if left <= right:
            MN[left], MN[right] = MN[right], MN[left]
            left += 1
            right -= 1
    
    return MN

B = [1, -2, 3, -4, -5, 6, -7, 8, -9]
print(move_negative_elements(B))
