y = 2 ** 1024 + 2 ** 1025


def f(x, cc):
    x_c = ''
    while x:
        x_c += str(x % cc)
        x //= cc
    # спросили про первую цифру, а вы не повернули число? - балл
    x_c = x_c[::-1]
    return x_c


number = f(y, 16)
print(number[0])
