# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lbound, rbound):
            # Node out of acceptable range
            if root.val >= rbound or root.val <= lbound:
                return False
            
            # check if its leaf node
            if root.left is None and root.right is None:
                return True
            elif root.left is None:
                return dfs(root.right, root.val, rbound)
            elif root.right is None:
                return dfs(root.left, lbound, root.val)
            else:
                return dfs(root.left, lbound, root.val) and dfs(root.right, root.val, rbound)
                
        return dfs(root, float(-inf), float(inf))

        