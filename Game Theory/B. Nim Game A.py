#check if first player can take lasta stone
#check if first player can result in even playing field
#check number of rows > 1
#check number of rows
'''
1 row = guaranteed win
2 row : bikin 2 row 1
1 2 : 2 rows, 1 over 1 = winning
2 2 : 2 rows 2 over 1 = losing
3 2 : 2 rows 2 over 1 = losing
1 1 : 2 rows 0 over = losing
1 1 1 : 3 rows 0 over = winning
1 2 1 : 3 rows 1 over = winning
'''


if __name__ == "__main__":
    n = int(input())
    temp = 0
    #if current playing field is even (XOR all), p1 lose
    inp = [int(x) for x in input().split(" ")]
    for i in inp:
        temp^= i
    if(temp==0):
        print("TIDAK")
    else:
        print("YA")
