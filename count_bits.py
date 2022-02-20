def countBits(self, n: int) -> List[int]:
    '''
    res = [0]*(n+1)
    for i in range(n+1):
        val = i
        count = 0
        while val:
            count += val & 1
            val = val >> 1
        res[i] = count
    return res
    '''
    offset = 1
    dp = [0] * (n+1)
    for i in range(1, n+1):
        if offset*2 == i:
            offset *= 2
        dp[i] = 1 + dp[i-offset]
    return dp