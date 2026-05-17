"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p,q
        while p1 != p2:
            p1 = q if p1.parent is None else p1.parent
            p2 = p if p2.parent is None else p2.parent
        return p1
        