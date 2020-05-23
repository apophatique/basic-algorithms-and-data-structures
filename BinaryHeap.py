class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i //= 2

    def percDown(self, i):
        while(i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        elif self.heapList[i*2] < self.heapList[i*2+1]:
            return i * 2
        else:
            return i * 2 + 1

    def insert(self, obj):
        self.heapList.append(obj)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def delMin(self):
        self.heapList[1] = self.heapList[self.currentSize - 1]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)

    def buildHeap(self, items):
        i = len(items) // 2
        self.currentSize = len(items)
        self.heapList = [0] + items[:]
        while i > 0:
            self.percDown(i)
            i = i - 1
