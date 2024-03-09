# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Inorder Traversal  : left ->root -> right
# Preorder Traversal : root, left , right
# Post Order traversal : left ,right , root
# Breadth First Search

def inorder(root,Ans):
    if(root == None):
        return
    
    inorder(root.left,Ans)
    Ans.append(root.val)
    inorder(root.right,Ans)

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return 0
        liste = []
        inorder(root,liste)
        diff = max(liste)
        for i in range(len(liste)-1):
            diff = min(diff,liste[i+1]-liste[i])
        return diff