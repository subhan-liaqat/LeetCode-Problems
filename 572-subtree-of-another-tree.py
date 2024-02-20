# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
    def preorder(root):
        if root is None:
            return False
        if check(root, subRoot):
            return True
        return preorder(root.left) or preorder(root.right)
    
    def check(root, subRoot):
        if not root and not subRoot: return True
        if root and subRoot and root.val == subRoot.val and check(root.left,subRoot.left)and check(root.right,subRoot.right):
            return True
        return False
    
    return preorder(root)
