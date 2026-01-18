# Solution for pablos-market-35a291a1
# Platform: hackerearth
# Date: 2026-01-18
#

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    N = int(next(it))
    prices = [int(next(it)) for _ in range(N)]
    Q = int(next(it))

    queries = []
    for i in range(Q):
        l = int(next(it)) - 1
        r = int(next(it)) - 1
        queries.append((l, r, i))

    if N == 0:
        for _ in range(Q):
            sys.stdout.write("0\n")
        return

    max_p = max(prices)
    spf = list(range(max_p + 1))
    for i in range(2, int(max_p**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, max_p + 1, i):
                if spf[j] == j:
                    spf[j] = i

    danger_vals = []
    for p in prices:
        d_cnt = 1
        temp = p
        while temp > 1:
            p_fact = spf[temp]
            count = 0
            while temp % p_fact == 0:
                count += 1
                temp //= p_fact
            d_cnt *= count + 1
        danger_vals.append(d_cnt)

    unique_d = sorted(list(set(danger_vals)))
    d_map = {val: i for i, val in enumerate(unique_d)}
    v = [d_map[x] for x in danger_vals]
    max_v = len(unique_d)

    block_size = int(N / (max(1, Q**0.5))) + 1
    queries.sort(
        key=lambda x: (
            x[0] // block_size,
            x[1] if (x[0] // block_size) % 2 == 0 else -x[1],
        )
    )

    ans = [0] * Q
    count = [0] * (max_v + 1)
    curr_l, curr_r = 0, -1
    curr_ans = 0

    for l, r, q_idx in queries:
        while curr_r < r:
            curr_r += 1
            val = v[curr_r]
            curr_ans += count[val]
            count[val] += 1
        while curr_l > l:
            curr_l -= 1
            val = v[curr_l]
            curr_ans += count[val]
            count[val] += 1
        while curr_r > r:
            val = v[curr_r]
            count[val] -= 1
            curr_ans -= count[val]
            curr_r -= 1
        while curr_l < l:
            val = v[curr_l]
            count[val] -= 1
            curr_ans -= count[val]
            curr_l += 1
        ans[q_idx] = curr_ans

    sys.stdout.write("\n".join(map(str, ans)) + "\n")


if __name__ == "__main__":
    solve()
