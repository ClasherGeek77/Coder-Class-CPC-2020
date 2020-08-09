'''
recursively search possible moves
selesain kaya fibonacci
https://www.youtube.com/watch?v=JT8ZuJey3s0
'''


class calc:
    arr = None
    n = 0

    def __init__(self, arr, n):
        self.arr = [[None for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(i, n):
                #self.arr[i][j] = [max(arr[i], arr[j]),0]
                self.arr[i][j] = max(arr[i], arr[j])

    def combgame(self, start, end):
        if self.arr[end][start] is not None:
            if(end==start):
                return [self.arr[end][start],0]
            return self.arr[end][start]
        posa = self.combgame(start + 1, end)
        posb = self.combgame(start, end - 1)
        # reverse resulted array
        posa = posa[::-1]
        posb = posb[::-1]

        #tambahin kantong diambil ke kemungkinan posisi a dan b
        posa[0] += self.arr[start][start]
        posb[0] += self.arr[end][end]

        #cek posisi a dan b yang lebi menguntungkan
        if (posa[0] > posb[0]):
            self.arr[end][start] = posa
            return posa
        self.arr[end][start] = posb
        return posb
        # return [p1,p2]


if __name__ == "__main__":
    n = int(input())
    res = calc([int(x) for x in input().split()], n)
    print(res.combgame(0, n-1)[0])