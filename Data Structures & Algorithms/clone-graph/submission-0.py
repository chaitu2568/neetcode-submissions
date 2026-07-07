"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return

        # Traverse the graph using BFS

        queue = deque()

        queue.append(node)

        visited = {}
        visited[node] = Node(node.val)

        while queue:

            curr = queue.popleft()

            for nei in curr.neighbors:

                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    queue.append(nei)
                
                visited[curr].neighbors.append(visited[nei])
        
        return visited[node]

                 


        