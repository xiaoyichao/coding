'''
https://leetcode.cn/problems/jump-game-ii/description/
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i] 
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。



初始化：

n：数组的长度。
end：初始化为 0，表示当前跳跃的边界。
farthest：初始化为 0，表示在当前跳跃范围内可以到达的最远位置。
jumps：初始化为 0，记录跳跃次数。
遍历数组：

遍历从索引 0 到 n - 2（不包括最后一个位置），因为如果你在倒数第二个位置已经能够跳到最后一个位置，则不需要再遍历最后一个位置。
更新 farthest：

farthest = max(nums[i] + i, farthest)：计算在当前索引 i 处可以跳跃到的最远位置，并更新 farthest。
检查是否需要跳跃：

if end == i：如果当前索引 i 达到了当前跳跃的边界 end，则说明需要进行一次跳跃。
jumps += 1：增加跳跃次数。
end = farthest：将当前跳跃的边界更新为可以到达的最远位置 farthest。
返回跳跃次数：

当遍历完成后，返回总的跳跃次数 jumps。

'''

# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        farthest = 0
        jumps = 0
        for i in range(n - 1):
            farthest = max(nums[i] + i, farthest)
            if end == i:
                jumps += 1
                end = farthest
        return jumps
# 详细解析参见：
# https://labuladong.online/algo/slug.html?slug=jump-game-ii
