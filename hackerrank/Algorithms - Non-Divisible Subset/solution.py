# https://www.hackerrank.com/challenges/non-divisible-subset?isFullScreen=true
def max_subset_size(k, X):
    counts = [0] * k
    for i in X:
        counts[i % k] += 1

    count = min(counts[0], 1)

    if k % 2 == 0:
        count += min(counts[k // 2], 1)

    count += sum(max(counts[i], counts[k - i]) for i in range(1, (k + 1) // 2))

    return count


print(max_subset_size(3, [1, 7, 2, 4]))
