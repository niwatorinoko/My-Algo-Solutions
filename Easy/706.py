class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            i = self.keys.index(key)
            self.values[i] = value

    def get(self, key: int) -> int:
        if key in self.keys:
            i = self.keys.index(key)
            return self.values[i]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if key in self.keys:
            i = self.keys.index(key)
            self.values.pop(i)
            self.keys.pop(i)