# coding=UTF-8
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/max-area-of-island/solution/dao-yu-de-zui-da-mian-ji-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

给你一个大小为 m x n 的二进制矩阵 grid 。

岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

岛屿的面积是岛上值为 1 的单元格的数目。

计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。



来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

# 深度优先搜索可以用递归或者栈实现

# 深度优先搜索也可以用来检测环路:记录每个遍历过的节点的父节点，若一个节点被再次遍 历且父节点不同，则说明有环。
# 我们也可以用之后会讲到的拓扑排序判断是否有环路，若最后存 在入度不为零的点，则说明有环。


from typing import List

# 方法一：递归的方式进行深度优先搜索
class Solution:
    # 复杂度分析
    # 时间复杂度：O(m×n)。其中 mm 是给定网格中的行数，nn 是列数。我们访问每个网格最多一次。
    # 空间复杂度：O(m×n)，栈中最多会存放所有的土地，土地的数量最多为  m×n 块，因此使用的空间为 O(m×n)。
    def dfs(self, grid, cur_i, cur_j) -> int:
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1: # 递归边界
            return 0
        else:  # 如果不是递归的边界情况，说明当前位置可以作为岛屿或者说陆地
            ans = 1  # 当次递归的ans（结果）记录为1 ，一块岛屿的面积为1 
            grid[cur_i][cur_j] = 0 # 遍历过的数据置为0
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                next_i, next_j = cur_i + di, cur_j + dj
                ans += self.dfs(grid, next_i, next_j)
            return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        # for i, l in enumerate(grid):
        #     for j, n in enumerate(l):
        for i in range(len(grid)): # 遍历二维数组的每一个数据点
            for j in range(len(grid[i])):
                ans = max(self.dfs(grid, i, j), ans)
        return ans

# 方法二：深度优先搜索 + 栈
#  python 的栈(Stack) 用list + pop()就可以实现, 队列用list + pop(0)就可以实现，当然也可以使用from collections import deque 的队列功能
class Solution:
    # 时间复杂度：O(m×n)。其中 mm 是给定网格中的行数，nn 是列数。我们访问每个网格最多一次。
    # 空间复杂度：O(m×n)，栈中最多会存放所有的土地，土地的数量最多为 m×n 块，因此使用的空间为 O(m×n)。
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        # for i, l in enumerate(grid): # 遍历二维数组
        #     for j, n in enumerate(l):
        for i in range(len(grid)): # 遍历二维数组中的每个数据点
            for j in range(len(grid[i])): 
                cur = 0  # 以每个数据都作为起点尝试一次
                stack = [(i, j)]
                while stack: # 当栈不为空的时候，就可以后续的计算
                    cur_i, cur_j = stack.pop()
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1: # 遍历的边界条件
                        continue
                    else: # 如果不是遍历的边界条件，那么当前的数据点可以作为岛屿或者陆地
                        cur += 1 # 岛屿面积+1
                        grid[cur_i][cur_j] = 0 # 当前位置使用过，置为0，防止重复计数
                        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]: # 上下左右四个方向
                            next_i, next_j = cur_i + di, cur_j + dj
                            stack.append((next_i, next_j)) # 压入栈，用于遍历他的相邻节点
                ans = max(ans, cur)
        return ans

# 方法三：广度优先搜索
# 我们把方法二中的栈改为队列，每次从队首取出土地，并将接下来想要遍历的土地放在队尾，就实现了广度优先搜索算法。
# 由于是按层次进行遍历，广度优先搜索时 按照“广”的方向进行遍历的，也常常用来处理最短路径等问题。
class Solution:
    # 时间复杂度：O(m×n)。其中 mm 是给定网格中的行数，nn 是列数。我们访问每个网格最多一次。
    # 空间复杂度：O(m×n)，队列中最多会存放所有的土地，土地的数量最多为 m×n 块，因此使用的空间为 O(m×n)。
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)): # 遍历二维数组中的每个数据点
            for j in range(len(grid[i])): 
                cur = 0
                q = [(i, j)]
                while q: #当队列不为空的时候，就可以进行后续的计算
                    cur_i, cur_j = q.pop(0)
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1: # 边界条件：超出二维数据的边界或者当前数据点=0
                        continue
                    cur += 1
                    grid[cur_i][cur_j] = 0
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i, next_j = cur_i + di, cur_j + dj
                        q.append((next_i, next_j))
                ans = max(ans, cur)
        return ans

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

s_1 = Solution()
ans = s_1.maxAreaOfIsland(grid)
print(ans)