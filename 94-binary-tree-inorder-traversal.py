# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result = []

        def inorder(root) :
            if not root:
                return
            else:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)
        inorder(root)
        return result
        # time complexity -->O(n)
        # space complexity -->O(n)
