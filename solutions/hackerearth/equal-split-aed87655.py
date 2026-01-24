# Solution for Naruto and Equal Split
# Platform: hackerearth
# Date: 2026-01-19
#
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    t_str = input_data[ptr]
    ptr += 1
    T = int(t_str)

    results = []
    for _ in range(T):
        N = int(input_data[ptr])
        ptr += 1
        weights = [int(x) for x in input_data[ptr : ptr + N]]
        ptr += N
        prices = [int(x) for x in input_data[ptr : ptr + N]]
        ptr += N

        total_p = sum(prices)
        total_w = sum(weights)
        half_n = N // 2

        dp = [{} for _ in range(half_n + 1)]
        dp[0][0] = 0

        for i in range(N):
            w_i = weights[i]
            p_i = prices[i]

            for j in range(min(i, half_n - 1), -1, -1):
                curr_dict = dp[j]
                next_dict = dp[j + 1]
                for w, p in curr_dict.items():
                    new_w = w + w_i
                    new_p = p + p_i
                    if new_p > next_dict.get(new_w, -1):
                        next_dict[new_w] = new_p

        max_val = 0.0
        final_states = dp[half_n]
        for w, p in final_states.items():
            current_avg_sum = (p / w) + (total_p - p) / (total_w - w)
            if current_avg_sum > max_val:
                max_val = current_avg_sum

        results.append(f"{max_val:.6f}")

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()
