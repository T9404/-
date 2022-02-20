# 1 Решение

f = open('27B.txt')
n = int(f.readline())


# H + Ч, Ч + Н

k_5 = [0, 0]  # четные, нечетные
k_other = [0, 0]  # четные, нечетные

for _ in range(n):
    x = int(f.readline())

    if x % 5 == 0:
        k_5[x % 2] += 1
    else:
        k_other[x % 2] += 1


print((k_5[0]*k_other[1]) + (k_5[1]*k_other[0]) + (k_5[0]*k_5[1]))









# 2 Решение

f = open('27B.txt')
n = int(f.readline())


count_5, count_other = [0, 0], [0, 0]
answer = 0

for i in range(n):
    x = int(f.readline())

    if (x % 5) == 0:
        answer += count_other[(x+1) % 2]
    else:
        answer += count_5[(x+1) % 2]

    if x % 5 == 0:
        count_5[x % 2] += 1

    count_other[x % 2] += 1


print(answer)
