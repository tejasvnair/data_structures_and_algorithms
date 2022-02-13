def minWindow(self, s: str, t: str) -> str:
    # Time complexity: O(m) => m = len(s)
    # Space complexity: O(n) => n = len(t)
    # Hashtable to track the window's characters
    window_s = {}
    # Hashtable to track t's characters
    hash_t = {}
    for c in t:
        hash_t[c] = 1 + hash_t.get(c, 0)
    have, need = 0, len(hash_t)
    
    # initialize the output substring index and length
    left, right, reslen = -1, -1, float("inf")
    # initialize left pointer
    l = 0
    for r in range(len(s)):
        c = s[r]
        if c in t:
            window_s[c] = 1 + window_s.get(c, 0)
            # increment "have" when character counts match with that of the count in t
            if window_s[c] == hash_t[c]: 
                have += 1
        
        while have==need:
            # keep moving the left pointer while counts in substring are equal to counts in t
            if (r-l+1) < reslen:
                # found a smaller valid substring
                # update indices of valid substring
                reslen = r-l+1
                left, right = l, r
            
            c = s[l]
            if c in t:
                # remove char from window hashtable as the left pointer is moving
                window_s[c] -= 1
                if window_s[c] < hash_t[c]:
                    # check if the count in window hashtable reduces below t's hashtable
                    # decrease "have" in this case
                    have -= 1
            l += 1
    
    return s[left:right+1]

            
