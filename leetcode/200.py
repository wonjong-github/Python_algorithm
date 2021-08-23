class Solution(object):
    def numIslands(self, grid:list[list[str]])->int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        def dfs(grid, visit, x, y):
            visit[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < len(grid) and nx >=0 and ny < len(grid[0]) and ny >= 0:
                    if grid[nx][ny] == "1" and visit[nx][ny] == 0:
                        dfs(grid, visit, nx, ny)


        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and visit[i][j]==0:
                    dfs(grid, visit, i, j)
                    answer+=1

        return answer

a = Solution()
a.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
