class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        # use priority queue with custom priorities to maintain
        # max frequency charecter as max queue

        pq = []

        if a > 0:
            heapq.heappush(pq,(-a, 'a')) #max heap push O(a+b+c) = O(1)
        
        if b > 0:
            heapq.heappush(pq,(-b, 'b'))
        
        if c > 0:
            heapq.heappush(pq,(-c, "c"))
        
        res = []
        
        while pq:

            curr_char_count, curr_char = heapq.heappop(pq)

            curr_char_count = -curr_char_count

            #to handle consequitve 3 constraint
            if len(res) >= 2 and res[-1] == curr_char and res[-2] == curr_char: 
                if not pq:
                    break
                #pop other char
                other_char_count, other_char = heapq.heappop(pq)
                res.append(other_char)
                temp_count = -other_char_count
                temp_count -= 1
                if temp_count > 0: #push other char if the freq is non-zero after decrementing
                    heapq.heappush(pq,(-temp_count,other_char))
            else:
                res.append(curr_char)
                curr_char_count -= 1

            if curr_char_count > 0: #push it back after decrementing frequency if more char exists
                heapq.heappush(pq,(-curr_char_count,curr_char))
        
        return "".join(res)

        