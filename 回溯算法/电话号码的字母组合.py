"https://leetcode.cn/problems/letter-combinations-of-a-phone-number/?favorite=2cktkvj"


from typing import List


class Solution:
    # 每个数字到字母的映射
    mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        # 从 digits[0] 开始进行回溯
        self.backtrack(digits, 0, [], res)
        return res
    
    # 回溯算法主函数
    def backtrack(self, digits: str, start: int, path: List[str], res: List[str]) -> None:
        if len(path) == len(digits):
            # 到达回溯树底部
            res.append("".join(path))
            return
        # 回溯算法框架
        for i in range(start, len(digits)):
            digit = int(digits[i])
            for c in self.mapping[digit]:
                # 做选择
                path.append(c)
                # 递归下一层回溯树
                self.backtrack(digits, i + 1, path, res)
                # 撤销选择
                path.pop()

