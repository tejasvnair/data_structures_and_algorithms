def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    num_map = {}
    res = []
    # Fill the map with freq of each number
    for n in nums:
        num_map[n] = 1 + num_map.get(n, 0)
    
    # 2D count list with each index corresponding to the frequency
    # which contains list of values with that corresponding freq
    count_list = [[] for i in range(len(nums)+1)]
    for num, count in num_map.items():
        count_list[count].append(num)
    
    count = 0 # keep track of the number of top elements to be returned
    for num_repeat in range(len(nums), -1, -1):
        if count_list[num_repeat] == []:
            continue
        for val in count_list[num_repeat]:
            res.append(val)
            count += 1
            if count == k:
                return res