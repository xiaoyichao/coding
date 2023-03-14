"https://leetcode.cn/problems/sort-array-by-parity/"

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1  # 初始化双指针 i 指向开头，j 指向结尾
        while i < j:  # 当 i 和 j 没有相遇时
            if nums[i]%2==0:  # 如果 nums[i] 是偶数
                i+=1  # i 向右移动一位
            elif nums[j]%2==1:  # 如果 nums[j] 是奇数
                j-=1  # j 向左移动一位
            else:  # 如果 nums[i] 是奇数，nums[j] 是偶数
                nums[i], nums[j] = nums[j], nums[i]  # 交换两个数的位置
                i+=1  # i 向右移动一位
                j-=1  # j 向左移动一位
        return nums  # 返回排好序的数组
