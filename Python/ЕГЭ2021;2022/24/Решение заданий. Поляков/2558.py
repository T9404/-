'''
Текстовый файл 24-s1.txt состоит не более чем из 106 заглавных латинских букв (A..Z). 
Текст разбит на строки различной длины. Определите количество строк, в которых встречается 
комбинация A*R, где звёздочка обозначает любой символ.
'''
# https://prnt.sc/Yf6ZvkDEgMr4


f = open('24-s1.txt')


count = 0


while True:
    s = f.readline()
    if not s:
        break

    for i in range(1, len(s) - 1):
        if s[i-1] == 'A' and s[i+1] == 'R':
            count += 1
            break


print(count)
