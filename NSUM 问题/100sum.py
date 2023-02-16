def nSumTarget(nums, n, start, target):
    sz = len(nums)
    res = []
    # 至少是 2Sum，且数组大小不应该小于 n
    if n < 2 or sz < n:
        return res
    # 2Sum 是 base case
    if n == 2:
        # 双指针那一套操作
        lo, hi = start, sz - 1
        while lo < hi:
            s = nums[lo] + nums[hi]
            left, right = nums[lo], nums[hi]
            if s < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif s > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
    else:
        # n > 2 时，递归计算 (n-1)Sum 的结果
        for i in range(start, sz):
            sub = nSumTarget(nums, n - 1, i + 1, target - nums[i])
            for arr in sub:
                # (n-1)Sum 加上 nums[i] 就是 nSum
                arr.append(nums[i])
                res.append(arr)
            while i < sz - 1 and nums[i] == nums[i + 1]:
                i += 1
    return res
