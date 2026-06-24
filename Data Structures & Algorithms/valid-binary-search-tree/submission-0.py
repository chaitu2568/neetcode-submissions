# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #follow inorder traversal of BST which must give result strictly in incresing order

        if not root:
            return True

        #iterative inorder traversal

        stack = []
        res = []

        while True:

            if root:
                stack.append(root)
                root = root.left
            
            else:
                if not stack:
                    break

                root = stack.pop()
                res.append(int(root.val))
                root = root.right
        
        for i in range(len(res)-1):

            if res[i] >= res[i+1]:
                return False
        
        return True
            
        