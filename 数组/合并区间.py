"https://leetcode.cn/problems/merge-intervals/"
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if  intervals[i][0] <= res[-1][1]: # 后边的车头可以怼进去前面的车位，则表示可以合并。
                res[-1][1] = max(res[-1][1],intervals[i][1])
            else:  # 不能怼进去的，就是一个新的车
                res.append(intervals[i])
        return res
            
