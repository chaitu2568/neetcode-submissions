class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []


        def dfs(left_count,right_count,stack):

            if left_count == n and right_count == n:
                res.append("".join(stack))
                return
            
            if left_count < n:
                stack.append("(")
                dfs(left_count + 1,right_count,stack)
                stack.pop()
            
            if left_count > right_count:
                stack.append(")")
                dfs(left_count,right_count+1,stack)
                stack.pop()
        
        dfs(0,0,[])

        return res

        