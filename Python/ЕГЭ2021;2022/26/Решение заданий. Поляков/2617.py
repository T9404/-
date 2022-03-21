f = open('data/26.txt')
s, n = map(int, f.readline().split())


dt = [int(f.readline()) for _ in range(n)]
dt.sort()


cand = []

scur, i = 0, 0

while scur < s:
    if scur+dt[i] <= s:
        scur += dt[i]
        i += 1
        cand.append(dt[i])
    else:
        break


count = i
file = s-scur+dt[i]

for j in range(i+1, len(dt)):
    if file >= dt[j]:
        cand.append(dt[j])

print(count, max(cand))
