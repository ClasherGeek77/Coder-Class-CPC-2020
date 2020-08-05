class node:
    parent = None
    size = 1

    #parent dicari secara lazy (diupdate pas diperluin)
    def getparent(self):
        if self.parent is None:
            return self
        self.parent = self.parent.getparent()
        return self.parent


if __name__ == "__main__":
    n, m = [int(x) for x in input().split(" ")]
    tree = {}
    total = 1
    for i in range(1, m + 1):
        a, b = [int(x) for x in input().split(" ")]

        #ambil parent node darai a
        if a in tree:
            x = tree[a].getparent()
        else:
            x = node()
        # ambil parent node darai b
        if b in tree:
            y = tree[b].getparent()
        else:
            y = node()

        '''
        cek kedua parent
        kalo sama, skip
        kalo beda, bkin parent node baru dengan size (parent a+parent b)
        '''
        if x != y:
            temp = node()
            temp.size = x.size + y.size
            total = max(total, temp.size)
            x.parent = temp
            y.parent = temp
            tree[a] = temp
            tree[b] = temp
    print(total * total)
