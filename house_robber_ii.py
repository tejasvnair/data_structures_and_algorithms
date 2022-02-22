def rob(self, nums: List[int]) -> int:
    # Time complexity: O(n)
    # max of values excluding last house and values excluding first house
    # nums[0] to handle edge case
    return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

def helper(self, nums):
    r1, r2 = 0, 0
    for n in nums:
        tmp = max(n + r1, r2)
        r1 = r2
        r2 = tmp
    return r2