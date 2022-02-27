def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Idea is to traverse in-order and add the kth element reached in-order
    
    cur = root
    n = 0
    stack = []
    
    while cur or stack:
        # keep going left 
        while cur:
            stack.append(cur)
            cur = cur.left
        
        #left sub-tree is empty
        cur = stack.pop()
        n += 1
        if n==k:
            return cur.val
        cur = cur.right
        
    