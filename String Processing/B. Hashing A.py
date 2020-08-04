import sys

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def hash(m):
    text = input()
    total = ABC.index(text[0]) % m
    di = 26
    for x in text[1::]:
        total = (di * ABC.index(x) + total) % m
        di *= 26
    return total


if __name__ == "__main__":
    n, m = [int(x) for x in input().split(" ")]
    cond = True
    dict = [False] * m
    for i in range(n):
        temp = hash(m)
        if (dict[temp]):
            cond = False
            break
        else:
            dict[temp] = True
    if cond:
        print("TIDAK")
    else:
        print("YA")
