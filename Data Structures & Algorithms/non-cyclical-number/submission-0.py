class Solution:
    def isHappy(self, n: int) -> bool:

        slow, fast = n, self.sum_digits(n)
    
        while fast != 1 and slow != fast:
            slow = self.sum_digits(slow)
            fast = self.sum_digits(self.sum_digits(fast))
        
        if fast == 1:
            return True
        
        return False
    

    def sum_digits(self, n):
        
        total = 0
        
        while n > 0:
            total += (n % 10)**2
            n //= 10
        
        return total
            