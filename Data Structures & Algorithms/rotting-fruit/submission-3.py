class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = []
        length = 0
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i,j))
                elif grid[i][j] ==1:
                    fresh +=1
                
        curr = 0
        
        print(queue)
        
        while queue:
            
            for i in range(len(queue)):
                
                c = queue.pop(0)
                directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]
                curr = fresh
                
                
                for dh, dv in directions:
                    if min(c[0]+dh, c[1]+dv) < 0 or c[0]+dh >= len(grid) or c[1]+dv >= len(grid[0]) or grid[c[0]+dh][c[1]+dv] == 0 or grid[c[0]+dh][c[1]+dv] == 2 or (c[0]+dh, c[1]+dv) in visited:
                        continue 
                    visited.add((c[0]+dh, c[1]+dv))
                    queue.append((c[0]+dh, c[1]+dv))
                    fresh -=1
            if len(queue)> 0:
                    length +=1
        print(length)
        if fresh > 0:
            return -1
        else:
            return length
    

        