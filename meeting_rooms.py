def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    # Time complexity: O(nlogn)
    # Sort intervals based on start times
    intervals.sort(key=lambda x: x[0])
    num_itvals = len(intervals)
    # Check if next interval overlaps with current interval
    for i in range(num_itvals-1):
        if intervals[i][1] > intervals[i+1][0]:
            return False
    return True

