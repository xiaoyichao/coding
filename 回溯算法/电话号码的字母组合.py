def letterCombinations(self, digits: str) -> List[str]:
    if not digits:
        return self.res
    # 从 digits[0] 开始进行回溯
    self.backtrack(digits, 0, "")
    return self.res

# 回溯算法主函数
def backtrack(self, digits, start, s):
    if len(s) == len(digits):
        # 到达回溯树底部
        self.res.append(s)
        return
    # 回溯算法框架
    for i in range(start, len(digits)):
        digit = int(digits[i])
        for c in self.mapping[digit]:
            # 做选择
            s += c
            # 递归下一层回溯树
            self.backtrack(digits, i + 1, s)
            # 撤销选择
            s = s[:-1]
