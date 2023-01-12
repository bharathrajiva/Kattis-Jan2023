n = int(input())
k = int(input())
l = []
x = []
for _ in range(k):
    l.append(input().split())
for i in range(len(l)):
    z = int(l[i][1]) * int(l[i][0])
    x.append(z)
print(int(sum(x) / n))