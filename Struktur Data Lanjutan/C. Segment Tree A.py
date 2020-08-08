import math
class seg_tree:
    arr = []
    lazy = []
    n = 0

    def __init__(self, arr, n):
        size = 4*n-1
        self.arr = [0] * size
        self.lazy = [0] * size
        self.createTree(arr, 0, n - 1, 0)
        self.n = n
        pass

    def createTree(self, arr, start, end, ind):
        if (start > end):
            return
        if (start == end):
            self.arr[ind] = arr[start]
            return
        mid = (start + end) // 2
        self.createTree(arr, start, mid, ind * 2 + 1)
        self.createTree(arr, mid + 1, end, ind * 2 + 2)
        self.arr[ind] = self.arr[ind * 2 + 1] + self.arr[ind * 2 + 2]

    def getSum(self, start, end):
        return self.treeSum(0, self.n - 1, start, end, 0)

    def treeSum(self, start, end, searchs, searche, ind):
        if (self.lazy[ind] != 0):
            if ((end - start) % 2 == 0):
                self.arr[ind] ^= self.lazy[ind]
            if (start != end):
                self.lazy[ind * 2 + 1] ^= self.lazy[ind]
                self.lazy[ind * 2 + 2] ^= self.lazy[ind]
            self.lazy[ind] = 0
        if (start > end or start > searche or end < searchs):
            return 0
        if (start >= searchs and end <= searche):
            return self.arr[ind]
        mid = (start + end) // 2
        return (self.treeSum(start, mid, searchs, searche, 2 * ind + 1) +
                self.treeSum(mid + 1, end, searchs, searche, 2 * ind + 2))

    def updateRange(self, start, end, val):
        val = 1 << val
        self.treeUpdate(0, self.n - 1, start, end, 0, val)

    def treeUpdate(self, start, end, upds, upde, ind, val):
        if (self.lazy[ind] != 0):
            if ((end - start) % 2 == 0):
                self.arr[ind] ^= self.lazy[ind]
            if (start != end):
                self.lazy[ind * 2 + 1] ^= self.lazy[ind]
                self.lazy[ind * 2 + 2] ^= self.lazy[ind]
            self.lazy[ind] = 0
        if (start > end or start > upde or end < upds):
            return
        if (start >= upds and end <= upde):
            if ((end - start) % 2 == 0):
                self.arr[ind] ^= val
            if (start != end):
                self.lazy[ind * 2 + 1] ^= val
                self.lazy[ind * 2 + 2] ^= val
            return
        mid = (start + end) // 2
        self.treeUpdate(start, mid, upds, upde, ind * 2 + 1, val)
        self.treeUpdate(mid + 1, end, upds, upde, ind * 2 + 2, val)
        self.arr[ind] = self.arr[ind * 2 + 1] + self.arr[ind * 2 + 2]


if __name__ == "__main__":
    '''arr = [1, 2, 3, 4, 5];
    n = 5;
    tree = seg_tree(arr, n)
    print(tree.getSum(0, 4))
    tree.updateRange(3, 3, 2)
    print(tree.getSum(0, 4))
    tree.updateRange(0, 3, 1)
    print(tree.getSum(1, 3))'''

    n, m = [int(x) for x in input().split(" ")]
    arr = [int(x) for x in input().split(" ")]
    tree = seg_tree(arr, n)

    for i in range(m):
        com = [int(x) for x in input().split(" ")]
        com[1] -= 1
        com[2] -= 1
        if (com[0] == 1):
            tree.updateRange(com[1], com[2], com[3])
        else:
            print(tree.getSum(com[1], com[2]))
    pass
