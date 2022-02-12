def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    
    # create a table which will be used to check complement
    complement_table = {}
    
    for i, num in enumerate(nums):
        complement = target-num
        if complement in complement_table:
            return [i, complement_table[complement]]
        else:
            complement_table[num] = i