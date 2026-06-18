class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # At Maximum, per hour it can eat with the rate of max(piles) bananas from each pile. 

        l,r = 1,max(piles)
        res = r

        while l <= r:

            speed = (l+r)//2 
            totalTime = 0

            for pile in piles:
                totalTime += math.ceil(pile / speed)
            
            if totalTime > h:
                l = speed+1 #we need to increase speed to reduce total time
            else:
                res = speed
                r = speed - 1 #we will see if further decressing speed helps to finish the piles in given time
        
        return res