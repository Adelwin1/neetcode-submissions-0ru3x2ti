class Solution:
    def solve(self, b: List[List[str]]) -> None:
        rows, cols = len(b), len(b[0])
        some = deque()

        for i in range(cols):
            if b[0][i] =='O':
                some.append((0,i))
                b[0][i] ='a'
            if b[rows-1][i] =='O':
                some.append((rows-1, i))
                b[rows-1][i] ='a'

        for j in range(rows):
            if b[j][0] =='O':
                some.append((j, 0))
                b[j][0] = 'a'
            if b[j][cols-1] =='O':
                some.append((j, cols-1))
                b[j][cols-1] = 'a'

        
        while some:
            r, c = some.popleft()

            di = [(0,1), (-1,0), (0,-1), (1,0)]

            for i, j in di:
                nr,nc  = r+i, j+c

                if nr<0 or nr>= rows or nc<0 or nc>= cols:
                    continue
                
                if b[nr][nc] == 'X':
                    continue 
                if b[nr][nc] == 'a':
                    continue
                b[nr][nc] = 'a'
                some.append((nr, nc))

        for i in range(rows):
            for j in range(cols):
                if b[i][j] =='O':
                    b[i][j] = 'X'
                if b[i][j]=='a':
                    b[i][j] = 'O'

        





      
