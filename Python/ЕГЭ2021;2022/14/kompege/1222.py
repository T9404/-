x = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
k_0 = k_5 = 0
while x:
    if x % 6 == 0:
        k_0 +=1
    elif x % 6 == 5:
        k_5 += 1
    x //= 6
print(abs(k_0-k_5))
