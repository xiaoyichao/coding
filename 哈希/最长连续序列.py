"https://leetcode.cn/problems/longest-consecutive-sequence/?favorite=2cktkvj"



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 创建一个哈希表，用于存储每个整数的最长连续序列的长度
        num_set = set(nums)
        max_len = 0
        # 遍历整个数组
        for num in num_set:
            # 如果当前整数不在哈希表中，那么我们就要更新它的最长连续序列的长度
            if num - 1 not in num_set:
                cur_num = num
                cur_len = 1
                # 更新每个整数的最长连续序列的长度时，我们要看它左边和右边的整数是否存在于哈希表中
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_len += 1
                max_len = max(max_len, cur_len)
        # 最后，遍历整个哈希表，找出最长的连续序列的长度
        return max_len
