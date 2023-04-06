"https://leetcode.cn/problems/design-hashmap"

class MyHashMap:
    def __init__(self):
        self.hashmap = [-1] * 1000001
        
    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        return self.hashmap[key]

    def remove(self, key: int) -> None:
        self.hashmap[key] = -1


obj = MyHashMap()
obj.put(1,1)
param_2 = obj.get(1)
obj.remove(1)