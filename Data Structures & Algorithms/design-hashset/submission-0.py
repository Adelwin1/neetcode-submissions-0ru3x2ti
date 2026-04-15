class MyHashSet:

    def __init__(self):
        self.seto = set()
    def add(self, key: int) -> None:
        self.seto.add(key)
        

    def remove(self, key: int) -> None:
        self.seto.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.seto


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)