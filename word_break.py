def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    dp = [False]*(len(s)+1)
    # bottom-up solution
    dp[len(s)] = True
    
    # checking if its possible to get matching words in the dictionary from end of string to beginning
    for i in range(len(s)-1, -1, -1):
        for w in wordDict:
            # Check if one of the word matches 
            if i + len(w) <= len(s) and s[i:i+len(w)]==w:
                dp[i] = dp[i+len(w)]
            if dp[i]:
                break
    return dp[0]
    