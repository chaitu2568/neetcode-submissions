class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        neighs = defaultdict(set)

        for edge in edges:
            neighs[edge[0]].add(edge[1])
            neighs[edge[1]].add(edge[0])
        
        parent = -1

        visited = [False for _ in range(n)]

        def dfs(curr,parent):

            if visited[curr]:
                return False

            visited[curr] = True
            for child in neighs[curr]:
                if child == parent:
                    continue

                if not dfs(child,curr):
                    return False
            
            return True
        
        return dfs(0,parent) and False not in visited




        