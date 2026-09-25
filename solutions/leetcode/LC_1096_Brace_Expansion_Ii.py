# Solution for 1096 Brace Expansion II
# Platform: LeetCode
# Date: 2026-09-25
#
class Solution:
    def braceExpansionII(self, exp: str) -> list[str]:
        drawer = []

        builder = [""]
        result_box = []

        for ch in exp:
            if ch.isalpha():
                builder = [word + ch for word in builder]

            elif ch == '{':
                drawer.append((result_box, builder))
                result_box = []
                builder = [""]

            elif ch == ',':
                result_box.extend(builder)
                builder = [""]

            elif ch == '}':
                inner_result = result_box + builder

                prev_result_box, prev_builder = drawer.pop()

                builder = [p + w for p in prev_builder for w in inner_result]
                result_box = prev_result_box

        final_result = set(result_box + builder)
        return sorted(list(final_result))
