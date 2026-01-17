# Solution for akash and dine
# Platform: codechef
# Date: 2026-01-17
#


# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    dish = list(map(int, input().split()))
    time = list(map(int, input().split()))

    dist = {}

    for d, t in zip(dish, time):
        val = dist.get(d, float("inf"))
        dist[d] = min(val, t)
    # print(dist)
    if len(dist) < k:
        print(-1)
    else:
        print(sum(list(sorted(list(dist.values())))[:k]))
