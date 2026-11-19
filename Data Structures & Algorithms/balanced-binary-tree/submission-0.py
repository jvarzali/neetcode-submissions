# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.balanced(root, 0) > -1

    def balanced(self, root: Optional[TreeNode], height: int) -> int:
        if root: 
            left = self.balanced(root.left, height)
            right = self.balanced(root.right, height)
        else: 
            return 0

        if left == -1 or right == -1 or abs(right - left) > 1:
            return -1
        
        return max(left, right) + 1