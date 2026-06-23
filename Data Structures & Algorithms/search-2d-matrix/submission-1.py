class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #double binary search

        m,n = len(matrix), len(matrix[0])

        low,high = 0,m-1

        #first binary search to run target row
        while low <= high:

            row = (low+high)//2

            #if current row's smallest is lower than target
            if target < matrix[row][0]:
                high = row - 1
            # if current row's largest is lower than target
            elif target > matrix[row][-1]:
                low = row + 1
            else:
                break
        
        row = (low+high)//2

        #second binary search to run target ele in target row

        low,high = 0,n-1

        while low <= high:
            mid = (low + high)//2

            if target < matrix[row][mid]:
                high = mid - 1
            
            elif target > matrix[row][mid]:
                low = mid + 1
            
            else:
                return True
        
        return False

            
        