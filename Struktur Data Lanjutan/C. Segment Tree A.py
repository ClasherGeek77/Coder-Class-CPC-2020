'''
segment tree with lazy propagation
source (modified): https://www.geeksforgeeks.org/lazy-propagation-in-segment-tree/
'''

class Tree:
    head = None

    def __init__(self, arr, n):
        self.head = self.CreateTree(arr, 0, n - 1)

    def printTree(self, n):
        print()
        for i in range(n):
            print(self.getSum(i, i))
        print()

    def CreateTree(self, arr, start, end):
        # out of range
        if (start > end):
            return
        # last node
        if (start == end):
            return Node(arr[start], [start, end])
        mid = (start + end) // 2
        curr = Node(ran=[start, end])
        curr.left = self.CreateTree(arr, start, mid)
        curr.right = self.CreateTree(arr, mid + 1, end)
        curr.updvalue()
        return curr

    def getSum(self, start, end):
        return self.head.getSum(start, end)

    def updateRange(self, start, end, val):
        val = 1 << val
        self.head.updateRange(start, end, val)


class Node:
    '''
    left, right => anak kiri dan kanan
    value => nilai Node
    ran => range yang dicakup segment tree
    mask => lazy variable buat nyimpen bit yang perlu di inverse
    isEven =>  cek total anaknya ganjil atau genap (kalo genap bit di inverse)
    ex :
        ran 0,0 berarti node cuma ngerepresentasi 1 data di array, jadi bit di inverse
        ran 0,1 berarti node ngerepresentasi 2 data di array, jadi bit di inverse 2x (ga ke inverse)
    isntlast => cek ini node terakhir bukan, kalo terakhir, ga cek anaknya lagi
    '''
    left = None
    right = None
    value = 0
    ran = None
    mask = 0
    iseven = False
    isntlast = False

    def __init__(self, x=0, ran=None):
        self.value = x
        self.ran = ran
        self.iseven = (ran[1] - ran[0]) % 2 == 0
        self.isntlast = not ran[1] == ran[0]

    def updvalue(self):
        self.value = self.left.value + self.right.value

    def getSum(self, start, end):
        # node diupdate dlu sesuai masknya
        if (self.mask != 0):
            if (self.iseven):
                self.value ^= self.mask
            if (self.isntlast):
                self.left.mask ^= self.mask
                self.right.mask ^= self.mask
            self.mask = 0
        if (self.outOfRange(start, end)):
            return 0
        if (self.inRange(start, end)):
            return self.value
        return self.left.getSum(start, end) + self.right.getSum(start, end)

    def outOfRange(self, start, end):
        return self.ran[0] > end or self.ran[1] < start

    def inRange(self, start, end):
        return self.ran[0] >= start and self.ran[1] <= end

    def updateRange(self, start, end, mask):
        if (self.mask != 0):
            if (self.iseven):
                self.value ^= self.mask
            if (self.isntlast):
                self.left.mask ^= self.mask
                self.right.mask ^= self.mask
            self.mask = 0
        if (self.outOfRange(start, end)):
            return
        if (self.inRange(start, end)):
            # kalo node ada dalem range, update node ini aja, anaknya ga diupdate smua
            if (self.iseven):
                self.value ^= mask
            if (self.isntlast):
                self.left.mask ^= mask
                self.right.mask ^= mask
            return
        # kalo node berada sebagian, update anak2nya
        self.left.updateRange(start, end, mask)
        self.right.updateRange(start, end, mask)
        self.updvalue()


def test():
    arr = [1, 2, 3, 4, 5]
    n = 5
    tree = Tree(arr, n)
    print(tree.getSum(0, 4))
    tree.updateRange(3, 3, 2)
    print(tree.getSum(0, 4))
    tree.updateRange(0, 3, 1)
    print(tree.getSum(1, 3))


def prod():
    n, m = [int(x) for x in input().split(" ")]
    arr = [int(x) for x in input().split(" ")]
    tree = Tree(arr, n)

    for i in range(m):
        com = [int(x) for x in input().split(" ")]
        com[1] -= 1
        com[2] -= 1
        if com[0] == 1:
            tree.updateRange(com[1], com[2], com[3])
        else:
            print(tree.getSum(com[1], com[2]))


if __name__ == "__main__":
    test()
    #prod()
