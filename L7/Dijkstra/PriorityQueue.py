from Dijkstra.DXHeap import DXHeap

class Pair:
    value = (0, 0)
    def __init__(self, p) -> None:
        self.pair = p
    def __lt__(self, other):
        return self.value[0] < other.value[0]

    def __le__(self, other):
        return self.value[0] <= other.value[0]

    def __eq__(self, other):
        return self.value[0] == other.value[0]

    def __ne__(self, other):
        return self.value[0] != other.value[0]

    def __gt__(self, other):
        return self.value[0] > other.value[0]

    def __ge__(self, other):
        return self.value[0] >= other.value[0]

    def __str__(self):
        return str(self.value[0])
    
class PriorityQueue:
    __heap = DXHeap(n=10)
    def pop(self):
        return self.__heap.pop().value

    def isEmpty(self):
        return len(self.__heap) <= 0

    def push(self, value):
        self.__heap.push(Pair(value))
    