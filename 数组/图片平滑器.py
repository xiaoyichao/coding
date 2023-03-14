"https://leetcode.cn/problems/image-smoother/"


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])  # 获取图像的行数和列数
        res = [[0] * n for _ in range(m)]  # 初始化结果数组
        
        for i in range(m):
            for j in range(n):
                count = 0  # 初始化单元格周围存在的单元格数量
                for x in range(max(0, i-1), min(m, i+2)):  # 获取该单元格周围的行数
                    for y in range(max(0, j-1), min(n, j+2)):  # 获取该单元格周围的列数
                        res[i][j] += img[x][y]  # 累加该单元格周围存在的单元格的像素值
                        count += 1  # 累加单元格周围存在的单元格数量
                res[i][j] //= count  # 计算该单元格的平均灰度值，并向下取整
        
        return res  # 返回平滑后的图像
