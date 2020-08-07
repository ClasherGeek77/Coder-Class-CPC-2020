'''
implement lazy update
cuma update parent aja, bit parent di inverse kalo child ganjil
parent kasi tanda

kalo anak mau di update, cek bit parent // pasang bit di pointer pas ngetraversal tree
'''


class node:
    left = None
    right = None
    value = None
    mask = 0
    delta = None
    updated = True
    ran = []

    def __init__(self, ran, val=None):
        self.value = val
        self.ran = ran
        self.delta = (ran[1] - ran[0]) % 2

    def calcVal(self, searchran, unupdated=False, mask=0):
        if self.ran[0] >= searchran[0] and self.ran[1] <= searchran[1]:
            # inside search range
            if unupdated:
                self.value ^= mask
                self.mask ^= mask
                self.updated = False
            return self.value
        if self.ran[0] > searchran[1] or self.ran[1] < searchran[0]:
            # outside of search range
            return 0
        if unupdated or not self.updated:
            self.updated = True
            self.value ^= mask
            mask ^= self.mask
            self.mask = 0
            return self.left.calcVal(searchran, True, mask) + self.right.calcVal(searchran, True, mask)
        return self.left.calcVal(searchran) + self.right.calcVal(searchran)

    def flipbit(self, searchran, mask):
        if self.ran[0] > searchran[1] or self.ran[1] < searchran[0]:
            # outside of search range
            return
        if self.ran[0] >= searchran[0] and self.ran[1] <= searchran[1]:
            # inside range
            self.mask ^= mask
            self.updated = False
            if (self.delta == 0):
                self.value ^= mask
            return
        self.left.flipbit(searchran, mask)
        self.right.flipbit(searchran, mask)
        self.value = self.left.value + self.right.value
        return


def createTree(arr, left: int, right: int) -> node:
    if left >= right:
        return node([left, left], arr[left])
    else:
        mid = (left + right) // 2
        temp = node([left, right])
        temp.left = createTree(arr, left, mid)
        temp.right = createTree(arr, mid + 1, right)
        temp.value = temp.left.value + temp.right.value
        return temp


class segment:
    head = None
    '''
    jangan pake array, pake linked list aja
    '''

    def __init__(self, arr):
        self.head = createTree(arr, 0, len(arr) - 1)

    def inverse(self, com):
        invbit = 1 << com[2]
        self.head.flipbit(com[0:2], invbit)
        pass

    def count(self, com):
        return self.head.calcVal(com)
        pass


if __name__ == "__main__":
    n, m = [int(x) for x in input().split(" ")]
    arr = [int(x) for x in input().split(" ")]
    tree = segment(arr)  # make tree from arr here // needs tree class

    for i in range(m):
        com = [int(x) for x in input().split(" ")]
        com[1] -= 1
        com[2] -= 1
        if (com[0] == 1):
            tree.inverse(com[1::])
        else:
            print(tree.count(com[1::]))
    pass
