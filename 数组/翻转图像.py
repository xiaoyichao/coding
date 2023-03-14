"https://leetcode.cn/problems/flipping-an-image/"

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        # 水平翻转
        for i in range(n):
            image[i] = image[i][::-1]
        # 反转
        for i in range(n):
            for j in range(n):
                image[i][j] = 1 - image[i][j]
        return image
