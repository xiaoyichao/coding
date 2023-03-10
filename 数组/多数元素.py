"https://leetcode.cn/problems/majority-element/"

from collections import defaultdict

def majorityElement(nums):
    dic = defaultdict(int)
    for num in nums:
        dic[num] += 1
    for key, value in dic.items():
        if value > len(nums) / 2:
            return key
        
def majorityElement(nums):
    # 也可以使用排序的方法，由于多数元素的数量大于数组长度的一半，所以排序后的中间元素一定是多数元素。
    nums.sort()
    return nums[len(nums) // 2]
