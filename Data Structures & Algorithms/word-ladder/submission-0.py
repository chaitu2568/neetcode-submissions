class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        adj_matrix = defaultdict(list)

        for word in wordList:

            for i in range(len(word)):

                key = word[:i] + "_" + word[i+1:]

                adj_matrix[key].append(word)
        
        visited = set()
        visited.add(beginWord)

        queue = deque()

        queue.append((beginWord, 1))

        while queue:

            curr, depth = queue.popleft()

            for i in range(len(curr)):

                node = curr[:i] + "_" + curr[i+1:]

                for nei in adj_matrix[node]:

                    if nei == endWord:
                        return depth + 1
                    
                    if nei in visited:
                        continue
                    
                    visited.add(nei)
                    queue.append((nei, depth + 1))
            
        
        return 0
            

        