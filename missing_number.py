def missingNumber(self, nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    numLen = len(nums)
    sums = numLen*(numLen+1)//2
    for i in range(numLen):
        sums -= nums[i]
    return sums

