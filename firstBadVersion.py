# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

    def firstBadVersion(self, versions) -> int:
    
        n = len(versions)
        
        lower, upper = 1, n

        while lower <= upper:
            
            middle = (lower + upper) // 2
        
            bad = versions[middle]
            
            if bad:
                result = middle
                upper = middle-1 
                
            if not bad:
                lower = middle+1
        
        # add 1 to result as this method indexes a list and we're looking for the nth element
        result+=1
        
        return result