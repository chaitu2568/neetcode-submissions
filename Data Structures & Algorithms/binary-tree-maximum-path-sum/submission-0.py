# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        self.res = float('-inf')
        
        '''
        Idea here is this DFS helper method identifies max path sum
        Each path is like without split (i.e.. either from left sub tree or right sub tree)
        Recursively, we then calculate gain or path sum from left sub tree and right sub trees without split and add it to 
        root node

        Similar to diameter of Binary tree where we just need to find max distance b/w
        any two nodes in binary tree
        '''
        def dfs(root):

            if not root:
                return 0
            
            left_gain_withoutsplit = dfs(root.left)
            right_gain_withoutsplit = dfs(root.right)

            #Avoid negative gains from both sub trees
            left_gain_withoutsplit = max(left_gain_withoutsplit,0)
            right_gain_withoutsplit = max(right_gain_withoutsplit,0)

            #now at each step you can calculate curr gain
            self.res = max(self.res,left_gain_withoutsplit+right_gain_withoutsplit+root.val)

            #now for a current node you have both left and right gains (path sums) without split

            #so pick either left or right gain which ever is max (can't pick up as it doesn't give you valid path)
            return max(right_gain_withoutsplit, left_gain_withoutsplit) + root.val
        
        dfs(root)

        return self.res



