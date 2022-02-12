def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    res = []
    # Edge cases
    # empty intervals
    if len(intervals)==0:
        res.append(newInterval)
        return res
    # empty newInterval
    if len(newInterval)==0:
        return intervals
    
    intlen = len(intervals)-1
    
    # if newInterval is after all the intervals and non overlapping
    if newInterval[0] > intervals[intlen][1]:
        res = res + intervals[0:]
        res.append(newInterval)
        return res
    
    # for rest of the cases
    for i in range(len(intervals)):
        # if newInterval is before the intervals[i] and non overlapping
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif intervals[i][1] >= newInterval[0]:
            # if there is overlap
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        else:
            # no overlap
            res.append(intervals[i])
    
    res.append(newInterval)
    return res
