'''
implement lazy update
cuma update parent aja, bit parent di inverse kalo child ganjil
parent kasi tanda

kalo anak mau di update, cek bit parent // pasang bit di pointer pas ngetraversal tree
'''


def inverse(arr, com):
    pass


def count(arr, com):
    print(sum(arr[com[0]:com[1]]))
    pass


if __name__ == "__main__":
    n, m = [int(x) for x in input().split(" ")]
    arr = [int(x) for x in input().split(" ")]
    tree = arr  # make tree from arr here // needs tree class
    for i in range(m):
        com = [int(x) for x in input().split(" ")]
        if (com[0] == 1):
            inverse(tree, com[1::])
        else:
            count(tree, com[1::])
        print(com)
    pass
