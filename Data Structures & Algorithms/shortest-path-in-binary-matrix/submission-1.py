class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = []
        length = 0
        if grid[0][0] != 1:
            length +=1
        else:
            return -1
        visited.add((0,0))
        queue.append((0,0))
        

        
        while queue:
            for i in range(len(queue)):
                c = queue.pop(0)
                if c[0] == len(grid)-1 and c[1] == len(grid[0])-1:
                    return length
                directions = [[0, -1], [-1, 0], [1, 0], [0, 1], [-1,1], [1,-1], [1, 1], [-1, -1]]
                for dh, dv in directions:
                    if min(c[0]+dh, c[1]+dv) < 0 or c[0]+dh >= len(grid) or c[1]+dv >= len(grid[0]) or grid[c[0]+dh][c[1]+dv] == 1 or (c[0]+dh, c[1]+dv) in visited:
                        continue 
                    visited.add((c[0]+dh, c[1]+dv))
                    queue.append((c[0]+dh, c[1]+dv))
            length +=1
        print(length)
        return -1
    

                
                    


        