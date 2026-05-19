# Read input from stdin
# Example: n = int(input())
# Example: arr = list(map(int, input().split()))

import math

t = int(input())

for _ in range(t):
    W, H = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    w, h = map(int, input().split())

    cur_w = x2 - x1
    cur_h = y2 - y1

    ans = float('inf')

    # Try fitting horizontally
    if cur_w + w <= W:
        need_left = max(0, w - x1)
        need_right = max(0, w - (W - x2))
        ans = min(ans, need_left, need_right)

    # Try fitting vertically
    if cur_h + h <= H:
        need_down = max(0, h - y1)
        need_up = max(0, h - (H - y2))
        ans = min(ans, need_down, need_up)

    if ans == float('inf'):
        print(-1)
    else:
        print(f"{ans:.9f}")