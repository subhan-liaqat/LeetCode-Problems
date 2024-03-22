# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      #lets find the given node and collect its ancestors 
      if not root or root == p or root==q :
        return root # either we've reached leaf without finding of found p or q 
      l = self.lowestCommonAncestor(root.left,p,q) # find p , q in left subtree 
      r = self.lowestCommonAncestor(root.right,p,q) # find p, q in right subtree 
      
      if l and r : # found target 1 in left and target 2 in right, current root is ancestor
        return root
      else : 
        return l or r # otherwise either l child is the common ancestor or r child is the common ancestor 

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         while root:
#             if root.val > p.val and root.val > q.val:
#                 root = root.left
#             elif root.val < p.val and root.val < q.val:
#                 root = root.right
#             else:
#                 return root
        