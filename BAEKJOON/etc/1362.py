from sys import stdin
input = stdin.readline

sn = 0
st = [":-)", ":-(", "RIP"]

while (n:=input().split()) != ["0", "0"]:
    o, w = map(int, n)
    while (m:=input().split()) != ["#", "0"]:
        if w > 0:
            if m[0] == "F":
                w += int(m[1])
            else:
                w -= int(m[1])
                
    sn += 1
    if (o * 0.5) < w < (o * 2):
        print(sn, st[0])
    elif w <= 0:
        print(sn, st[2])
    else:
        print(sn, st[1])