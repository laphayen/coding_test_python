N, M = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
lt = 0
rt = N-1
while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == M:
        print(mid+1)
        break
    elif a[mid] > M:
        rt = mid - 1
    else:
        lt = mid + 1