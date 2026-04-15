
class Solution:
    def isValidSudoku(self, nums: List[List[str]]) -> bool:
        
        n_rows = len(nums)
        n_cols = len(nums[0])
    
        for i in range(n_rows):
            rows = set()
            for j in range(n_cols):
                num = nums[i][j]
                if num == '.':
                    continue
                if num in rows:
                    return False
                else:
                    rows.add(num)
        
        for j in range(n_cols):
            cols = set()
            for i in range(n_rows):
                num = nums[i][j]
                if num =='.':
                    continue
                if num in cols:
                    return False
                else:
                    cols.add(num)

        for a in range(0, 9, 3):
            for b in range(0, 9,3):
                grid = set()
                for i in range(3):
                    for j in range(3):
                        want = nums[a+i][b+j]
                        if want== '.':
                            continue
                        if want in grid:
                            return False
                        else:
                            grid.add(want)
        return True
                    

                