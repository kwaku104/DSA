from random import randint


class HashTable():
    def __init__(self, size) -> None:
        self.size = size
        self.data = [None] * self.size

    def _hashFunction(self, key):
        _hash = 0
        key = str(key)
        for i in range(len(key)):
            _hash = (_hash + ord(key[i]) * i) % len(self.data)
        return _hash

    def set(self, key, value):
        address = self._hashFunction(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, value):
        address = self._hashFunction(key)
        currentBucket = self.data[address]
        if currentBucket:
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    return currentBucket[i][0]
        return None


myHashTable = HashTable(5)
print(myHashTable.set('grapes', 1000))
print(myHashTable.set('apples', 1000))
print(myHashTable.set('banana', 1000))
print(myHashTable.set('pie', 1000))
