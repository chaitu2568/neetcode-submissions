class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        #maxheap maintain these to reduce idle time in between the tasks
        #because if you select less frequent tasks by leaving more frequent tasks
        #at last. Then, you need have more idle cpu cycles wasted to complete those identical 
        #frequent tasks that is leftover

        dics = Counter(tasks)

        maxheap = [(-value,key) for key,value in dics.items()]

        heapq.heapify(maxheap)

        cycles = 0

        while maxheap:

            waiting = []
            cooling_time = n+1

            while cooling_time and maxheap:

                cycles += 1

                freq,val = heapq.heappop(maxheap)

                if -freq > 1:
                    waiting.append((freq+1,val))
                
                cooling_time -= 1
            

            for wait in waiting:
                heapq.heappush(maxheap,wait)
            
            #if still maxheap, then count remaining idle time
            if maxheap:
                cycles += cooling_time #push remaining time as idle time
        
        return cycles


        

        