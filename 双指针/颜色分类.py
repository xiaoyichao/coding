"https://leetcode.cn/problems/sort-colors/"

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red , white, blue = 0, 0 , len(nums)-1
        while white<=blue:
            if nums[white] == 0: #当前元素是红色
                nums[red],nums[white] = nums[white], nums[red]
                red+=1
                white+=1
            elif nums[white] ==1: #当前说白色
                white+=1
            else: #当前是黑色
                nums[blue],nums[white] = nums[white], nums[blue]
                blue-=1
        return nums