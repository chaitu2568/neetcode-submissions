class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])

        def dfs(row,col,word):

            #base case 
            if len(word) == 1 and board[row][col] == word[0]:
                return True
            
            if board[row][col] == word[0]:

                #mark curr letter as visited
                board[row][col] = "*"

                for nr,nc in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:

                    if 0<=nr<rows and 0<=nc<cols and board[nr][nc] != "*":
                        
                        if dfs(nr,nc,word[1:]):
                            return True
                
                #mark curr letter as not visited
                board[row][col] = word[0]
            
            return False

        for row in range(rows):

            for col in range(cols):

                if board[row][col] == word[0] and dfs(row,col,word):
                    return True
        
        return False
        



        