

'''
桶排序适用的场景并不多，用得多一点的是基于桶排序思想的计数排序和基数排序。

1. 求出待排序列表中的最大值和最小值，得到数据的范围。

2. 根据数据的范围，选择一个适合的值构建有限数量的桶，确定每个桶的数据范围。如数据范围是[0,100)，将数据分成10个桶，第一个桶为[0,10)，第二个桶为[10,20)，以此类推。

3. 将待排序列表中的数据分配到对应的桶中。

4. 对每一个桶内的数据进行排序，这里可以采用任意一种排序算法，建议采用时间复杂度小的排序算法。

5. 将所有桶中的数据依次取出，添加到一个新的有序序列中，列表排序完成。
————————————————
版权声明：本文为CSDN博主「小斌哥ge」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43790276/article/details/107398295
'''

# bucket_sort 代码实现

from typing import List
import math
def bucket_sort(arr:List[int]):
    """桶排序"""
    min_num = min(arr)
    max_num = max(arr)
    # 桶的大小
    # bucket_range = (max_num-min_num) // len(arr) + 1
    bucket_range = math.ceil((max_num-min_num) / len(arr)) # 向上取整
    # 桶数组
    count_list = [ [] for i in range(len(arr) + 1)]
    # 向桶数组填数
    for i in arr:
        tmp = int((i-min_num)/bucket_range) # 向下取整，确定数据应该放入第几个桶
        count_list[tmp].append(i)
    arr.clear()
    # 回填，这里桶内部排序直接调用了sorted
    for i in count_list:
        for j in sorted(i):  #  i 表示第 i 个桶，j 表示对桶内数据排序后的第 j 个数据。
            arr.append(j)

# 测试数据

if __name__ == '__main__':

    arr = [1,1,1,2,2,3,2]
    print("原始数据：", arr)
    bucket_sort(arr)
    print("桶排序结果：", arr)