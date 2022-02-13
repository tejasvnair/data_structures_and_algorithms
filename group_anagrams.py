def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # Time complexity: O(n*m)
    # where n is total number of strings in strs
    # and m is average length of each string in strs
    # Use hash_map to track strings with same characters
    # Using count of each character as an indicator for anagram
    hash_map = defaultdict(list)
    for i in range(len(strs)):
        count = [0] * 26 # count of each character from a to z
        for c in strs[i]:
            count[ord(c)-ord("a")] += 1
        # append strs[i] to appropriate key value (based on count array)
        hash_map[tuple(count)].append(strs[i])
    return hash_map.values()