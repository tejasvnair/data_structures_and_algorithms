def hammingWeight(self, n: int) -> int:
    # Time complexity: O(1)
    # Space complexity: O(1)
    count = 0
    while n:
        count += n & 1
        n = n >> 1
    return count

    