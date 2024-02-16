# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if each or both are null
        if(p==None or q==None):
            return (p==q)
        
        # if root node's value and left and right sub-trees are equal
        return (p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
