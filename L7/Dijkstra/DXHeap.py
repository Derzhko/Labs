#  ужас просто

class DXHeap:
    def __init__(self, items=(), *, n=2, direction=min):
        self._n = n
        self._list = []
        self._direction = direction
        for item in items:
            self.push(item)

    def _parent_ix(self, ix):
        return (ix - 1) // self._n

    def _children_ix(self, ix):
        first_child = ix * self._n + 1
        return range(first_child, min(first_child + self._n, len(self._list)))

    def _sift_towards_root(self, ix):
        current = self._list[ix]
        while ix: 
            parent_ix = self._parent_ix(ix)
            parent = self._list[parent_ix]
            if self._direction(parent, current) is parent:
                return 
            self._list[parent_ix], self._list[ix], ix = current, parent, parent_ix

    def _sift_towards_leaf(self, ix):
        current = self._list[ix]
        while True:
            children = tuple((self._list[x], x) for x in self._children_ix(ix))
            if not children:
                return
            candidate, candidate_ix = self._direction(children)
            if self._direction(current, candidate) is current:
                return 
            self._list[candidate_ix], self._list[ix], ix = current, candidate, candidate_ix

    def __len__(self):
        return len(self._list)

    def push(self, item):
        self._list.append(item)
        self._sift_towards_root(len(self._list) - 1)

    def peek(self):
        return self._list[0]

    def pop(self):
        result, self._list[0] = self._list[0], self._list[-1]
        self._list.pop()
        if self._list:
            self._sift_towards_leaf(0)
        return result
