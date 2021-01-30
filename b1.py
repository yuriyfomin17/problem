def maxDifference(px):  # function definition
    maxDiff = -1
    for i in range(1, len(px)):  # accessing elements in px from 2 to last.
        for j in range(i - 1, -1, -1):  # accessing elements from i to first.
            if px[i] > px[j] and (
                    px[i] - px[j]) > maxDiff:  # if any element is less than and difference is more than maxDiff
                maxDiff = px[i] - px[j]  # updating max difference.
    return maxDiff  # returning max difference.


print(maxDifference([7, 1, 2, 5]))
