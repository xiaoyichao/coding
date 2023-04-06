"https://leetcode.cn/problems/reverse-words-in-a-string/description"

class Solution:
    def reverseWords(self, s: str) -> str:
        # 去掉开头和结尾的空格
        s = s.strip()
        # 将整个字符串翻转过来
        s = s[::-1]
        # 初始化结果字符串和当前单词
        res, word = '', ''
        # 遍历翻转后的字符串
        for c in s:
            # 遇到空格，将之前的单词进行翻转，并加入结果字符串中
            if c == ' ':
                if word:
                    res += word[::-1] + ' '
                    word = ''
            # 遇到非空格字符，将其加入当前单词中
            else:
                word += c
        # 最后一个单词可能没有空格分隔，所以需要单独对其进行翻转，并加入结果字符串中
        if word:
            res += word[::-1]
        return res
    
so = Solution()
so.reverseWords("the sky is blue")
