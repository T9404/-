f = open('27b.txt')
N = int(f.readline())


s = {0: 0}


for i in range(N):
    x = int(f.readline())

    c = [sm + x for sm in s.values()] + [x] + list(s.values())
    s = {x % 100: x for x in sorted(c)}


print(s[50])
