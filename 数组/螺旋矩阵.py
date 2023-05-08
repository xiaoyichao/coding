
"https://leetcode.cn/problems/spiral-matrix/"


from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    m = len(matrix)
    n = len(matrix[0])
    upper_bound = 0
    lower_bound = m - 1
    left_bound = 0
    right_bound = n - 1
    res = []
    # res.length == m * n 则遍历完整个数组
    while len(res) < m * n:
        if upper_bound <= lower_bound:
            # 在顶部从左向右遍历
            for j in range(left_bound, right_bound + 1):
                res.append(matrix[upper_bound][j])
            # 上边界下移
            upper_bound += 1
        
        if left_bound <= right_bound:
            # 在右侧从上向下遍历
            for i in range(upper_bound, lower_bound + 1):
                res.append(matrix[i][right_bound])
            # 右边界左移
            right_bound -= 1
        
        if upper_bound <= lower_bound:
            # 在底部从右向左遍历
            for j in range(right_bound, left_bound - 1, -1):
                res.append(matrix[lower_bound][j])
            # 下边界上移
            lower_bound -= 1
        
        if left_bound <= right_bound:
            # 在左侧从下向上遍历
            for i in range(lower_bound, upper_bound - 1, -1):
                res.append(matrix[i][left_bound])
            # 左边界右移
            left_bound += 1
    
    return res
