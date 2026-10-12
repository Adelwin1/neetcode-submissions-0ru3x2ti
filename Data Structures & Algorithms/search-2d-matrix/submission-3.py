class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
    
        n = len(m[0])

        for row in m:
            if row[n-1]<target:
                continue 

            l, r = 0, n-1

            while l<=r:
                mid = (l+r)//2

                if row[mid] == target:
                    return True 
                elif row[mid]< target:
                    l = mid+1
                else:
                    r = mid-1
        return False


        
        
    
                
                
        