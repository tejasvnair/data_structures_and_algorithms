def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # Time complexity: O(logN)
    cur = root
    while cur:
        if p.val < cur.val and q.val < cur.val:
            # both nodes on the left sub-tree
            cur = cur.left
        elif p.val > cur.val and q.val > cur.val:
            # both nodes on the right sub-tree
            cur = cur.right
        else:
            # cur node splits the two nodes or is one of the two nodes
            return cur
            