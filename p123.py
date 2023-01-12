

if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    r_q, c_q = map(int, input().strip().split())

    u_s = n - r_q
    r_s = n - c_q
    d_s = r_q - 1
    l_s = c_q - 1
    l_u_s = min(l_s, u_s)
    r_u_s = min(u_s, r_s)
    l_d_s = min(d_s, l_s)
    r_d_s = min(r_s, d_s)

    for _ in range(0, k):
        x, y = map(int, input().strip().split())

        if x == r_q and y < c_q and int(y - c_q) - 1 < l_s:
            l_s = int(y - c_q) - 1
        if x == r_q and y > c_q and int(y - c_q) - 1 < r_s:
            r_s = int(y - c_q) - 1
        if y == c_q and x < r_q and int(x - r_q) - 1 < d_s:
            d_s = int(x - r_q) - 1
        if y == c_q and x > r_q and int(x - r_q) - 1 < u_s:
            u_s = int(x - r_q) - 1

        if int(x - r_q) == int(y - c_q):
            if x > r_q and y < c_q and int(x - r_q) - 1 < l_u_s:
                l_u_s = int(x - r_q) - 1
            if x < r_q and y < c_q and int(x - r_q) - 1 < l_d_s:
                l_d_s = int(x - r_q) - 1
            if x < r_q and y > c_q and int(x - r_q) - 1 < r_d_s:
                r_d_s = int(x - r_q) - 1
            if x > r_q and y > c_q and int(x - r_q) - 1 < r_u_s:
                r_u_s = int(x - r_q) - 1

    total_moves = r_s + l_s + u_s + d_s + l_d_s + l_u_s + r_u_s + r_d_s

    print(total_moves)