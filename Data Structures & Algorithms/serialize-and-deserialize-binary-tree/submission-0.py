# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root:
            return "None"
        
        #preorder traversal (root,left,right) technique using iteration (not recursive)
        stack = [root]
        res = ""

        while stack:

            node = stack.pop()

            if node:
                res += str(node.val)+","
                stack.append(node.right)
                stack.append(node.left) # first left will be popped out
            else:
                res += "None,"
        
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        #get the root node as first element in data
        nodes = data.split(",")

        def helper(nodes):

            if not nodes:
                return

            curr = nodes.pop(0)

            if curr == "None":
                return None
            
            root = TreeNode(curr)
            root.left = helper(nodes)
            root.right = helper(nodes)

            return root
        
        return helper(nodes)



