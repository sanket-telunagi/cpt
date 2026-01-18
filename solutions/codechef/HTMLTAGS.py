# Solution for html tags
# Platform: codechef
# Date: 2026-01-18
#


def matchit(body):
    for val in body:
        if val in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False
    return True


for _ in range(int(input())):
    s = input().strip()
    # print(s[2:-1])

    body = s[2:-1]
    if (
        s
        and body
        and s.startswith("</")
        and s.endswith(">")
        and body.isalnum()
        and matchit(body)
    ):
        print("Success")
    else:
        print("Error")
