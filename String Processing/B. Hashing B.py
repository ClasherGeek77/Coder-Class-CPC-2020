
#BELOM SELESAI, TLE dan WA

if __name__ == "__main__":
    n = int(input())
    s = input()
    length = 1
    for i in range(n):
        for j in range(i + 1, n):
            ran = j - i
            if ran < n - j:
                subs = s[i:j]
                delt = j - i
                count = 0
                x, y = i, j
                while s[x:y] == subs:
                    x += delt
                    y += delt
                    count += 1
                    if y > n:
                        break
                length = max(length, count)
    print(length)