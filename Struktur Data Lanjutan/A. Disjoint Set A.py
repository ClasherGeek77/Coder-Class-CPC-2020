class node:
    parent = None

    def getparent(self):
        if self.parent is None:
            return self
        self.parent = self.parent.getparent()
        return self.parent


if __name__ == "__main__":
    n, m = [int(x) for x in input().split(" ")]
    # tree = []*(n+1)
    tree = {}
    cycle = -1
    for i in range(1, m + 1):
        a, b = [int(x) for x in input().split(" ")]
        if a in tree:
            x = tree[a].getparent()
        else:
            x = node()
        if b in tree:
            y = tree[b].getparent()
        else:
            y = node()
        if x == y:
            cycle = i
            break
        temp = node()
        x.parent = temp
        y.parent = temp
        tree[a] = temp
        tree[b] = temp
    print(cycle)
