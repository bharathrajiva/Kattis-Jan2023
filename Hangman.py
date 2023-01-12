n = input()
m = input()
c , res = 10,0
for i in m:
    if i not in n:
        c -= 1
    else:
        res += 1
    if res == len(set(n)):
        print('WIN')
        break
    if c == 0:
        print('LOSE')
        break
k= 5
obstacles = []
for _ in range(k):
        t, o = map(int, input().strip().split())
        h = [t, o]
        obstacles.append(h)
print(obstacles)