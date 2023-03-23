回溯算法可以解决 子集、排列、组合问题 

其实回溯算法和我们常说的 DFS 算法非常类似，本质上就是一种暴力穷举算法。回溯算法和 DFS 算法的细微差别是：回溯算法是在遍历「树枝」，DFS 算法是在遍历「节点」

实际上就是一个决策树的遍历过程，站在回溯树的一个节点上，你只需要思考 3 个问题：

1、路径：也就是已经做出的选择。

2、选择列表：也就是你当前可以做的选择。

3、结束条件：也就是到达决策树底层，无法再做选择的条件。


# labuladong 的总结

排列问题，拿到结果里边，诶个子结果和nums的长度都相同
组合问题，每个子结果的长度，根据题目设定，因此会设定start和k
子集问题，每个子结果的长度，从0-len(nums)都有。



result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
    
return result

其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」，特别简单。
回溯算法就是个多叉树的遍历问题，关键就是在前序遍历和后序遍历的位置做一些操作，


形式一、元素无重不可复选，即 nums 中的元素都是唯一的，每个元素最多只能被使用一次

/* 组合/子集问题回溯算法框架 */
def backtrack(nums, start, track):
    # 回溯算法标准框架
    for i in range(start, len(nums)):
        # 做选择
        track.append(nums[i])
        # 注意参数
        backtrack(nums, i + 1, track)
        # 撤销选择
        track.pop()


/* 排列问题回溯算法框架 */
def backtrack(nums, track, used):
    for i in range(len(nums)):
        # 剪枝逻辑
        if used[i]:
            continue
        # 做选择
        used[i] = True
        track.append(nums[i])

        backtrack(nums, track, used)
        # 撤销选择
        track.pop()
        used[i] = False


形式二、元素可重不可复选，即 nums 中的元素可以存在重复，每个元素最多只能被使用一次，其关键在于排序和剪枝

组合/子集问题回溯算法框架
nums.sort()

def backtrack(nums, start, track):
    # 回溯算法标准框架
    for i in range(start, len(nums)):
        # 剪枝逻辑，跳过值相同的相邻树枝
        if i > start and nums[i] == nums[i - 1]:
            continue
        # 做选择
        track.append(nums[i])
        # 注意参数
        backtrack(nums, i + 1, track)
        # 撤销选择
        track.pop()


排列问题回溯算法框架
nums.sort()

def backtrack(nums, track, used):
    for i in range(len(nums)):
        # 剪枝逻辑
        if used[i]:
            continue
        # 剪枝逻辑，固定相同的元素在排列中的相对位置
        if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
            continue
        # 做选择
        used[i] = True
        track.append(nums[i])

        backtrack(nums, track, used)
        # 撤销选择
        track.pop()
        used[i] = False


形式三、元素无重可复选，即 nums 中的元素都是唯一的，每个元素可以被使用若干次，只要删掉去重逻辑即可
组合/子集问题回溯算法框架
def backtrack(nums, start, track):
    # 回溯算法标准框架
    for i in range(start, len(nums)):
        # 做选择
        track.append(nums[i])
        # 注意参数
        backtrack(nums, i, track)
        # 撤销选择
        track.pop()


排列问题回溯算法框架
def backtrack(nums, track):
    for i in range(len(nums)):
        # 做选择
        track.append(nums[i])
        backtrack(nums, track)
        # 撤销选择
        track.pop()

