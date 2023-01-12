n = int(input())

def box(x, y, z):
    if n > x >= 0 and n > y >= 0 and z[x][y] == -1:
        return True
    return False


def fsol(n, z):
    for i in range(n):
        for j in range(n):
            print(z[i][j], end=' ')
        print()


def msol(n):
    z = [[-1 for i in range(n)] for i in range(n)]
    x_set = [2, 1, -1, -2, -2, -1, 1, 2]
    y_set = [1, 2, 2, 1, -1, -2, -2, -1]
    z[0][0] = 0
    k = 1
    if (not rsol(n, z, 0, 0, x_set, y_set, k)):

        print("OOps cant find one bud")
    else:
        fsol(n, z)


def rsol(n, z, i_x, i_y, move_x, move_y, k):
    if k == n ** 2:
        return True
    for i in range(8):
        q = i_x + move_x[i]
        p = i_y + move_y[i]
        if box(q, p, z):
            z[q][p] = k
            if rsol(n, z, q, p, move_x, move_y, k + 1):
                return True
            z[q][p] = -1
    return False



msol(n)
