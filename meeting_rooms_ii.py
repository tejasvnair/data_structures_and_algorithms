def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    # Getting the start and end times in an array
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])
    
    # pointers to the start and end arrays
    s, e = 0, 0
    res, count = 0, 0
    
    # loop over each start time, increment count when new meeting starts, decrement count when a meeting ends
    while s < len(intervals):
        if start[s] < end[e]:
            # New meeting starts
            s += 1
            count += 1
        else:
            # meeting ends
            e += 1
            count -= 1
        res = max(res, count)
    
    return res
    