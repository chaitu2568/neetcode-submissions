class Solution:
    def compress(self, chars: List[str]) -> int:

        n = len(chars)
    
        write, read = 0, 0
        
        while read < n:
            
            j = read
            count = 0
            
            while j < n and chars[read] == chars[j]:
                count += 1
                j += 1
            
            chars[write] = chars[read]
            write += 1
            
            if count > 1:
                for ch in str(count):
                    chars[write] = ch
                    write += 1
                    
            read = j
        
        return write
                
            
        