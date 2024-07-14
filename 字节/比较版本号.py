"https://leetcode.cn/problems/compare-version-numbers/"

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        i = 0
        j = 0
        while i<len(version1) or j<len(version2):
            if i<len(version1):
                v1 = int(version1[i])
            else:
                v1=0
            if j<len(version2):
                v2 = int(version2[i])
            else:
                v2=0

            if v1<v2:
                return -1
            elif v1>v2:
                return 1
            else:
                i+=1
                j+=1
        return 0


# GPT的做法
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        n1, n2 = len(v1), len(v2)
        max_len = max(n1, n2)
        for i in range(max_len):
            x = v1[i] if i < n1 else 0
            y = v2[i] if i < n2 else 0
            if x < y:
                return -1
            elif x > y:
                return 1
        return 0
