def rob(self, nums: List[int]) -> int:
    r1, r2 = 0, 0
    # dynamic prog solution: find max rob till each house
    # Time complexity: O(n)
    for n in nums:
        tmp = max(n+r1, r2)
        r1 = r2
        r2 = tmp
    return r2