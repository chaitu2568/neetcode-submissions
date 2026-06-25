# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        res = []

        #inorder traversal

        while True:

            if root:
                stack.append(root)
                root = root.left
            
            else:
                if not stack:
                    break 
                root = stack.pop()
                res.append(root.val)
                root = root.right

        return res[k-1]

        