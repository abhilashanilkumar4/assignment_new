def count_pairs_with_given_sum(a, target_sum):

    n = len(a)
    count = 0
    freq = {}
    for num in a:
        freq[num] = freq.get(num, 0) + 1

    for i in range(n):
        complement = target_sum - a[i]
        if complement in freq and freq[complement] > 0:
            count += freq[complement]
            freq[complement] -= 1
    return count

a = [1, 5, 7, -1, 5]
target_sum = 6
print(count_pairs_with_given_sum(a, target_sum)) 
