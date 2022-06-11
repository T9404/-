'''
Текстовый файл 24-178.txt состоит не более чем из 106 символов и содержит только заглавные 
буквы латинского алфавита (A..Z). Строка замыкается в кольцо, то есть за последним символом 
снова идёт первый. Определите в таком кольце максимальную длину цепочки, в которой все символы 
расположены в алфавитном порядке (одинаковые символы могут стоять рядом). Например, для строки 
CDEABCABC ответом будет 6 (цепочка ABCCDE).
'''
# https://prnt.sc/07abZsPTO0Vd


f = open('24.txt')

# убираем '\n'
s = f.readline()[:-1]
s += s


answer = 0

for i in range(len(s)):
    strin, start = s[i],  s[i]
    j = i + 1

    while j < len(s):
        if ord(s[j]) >= ord(start):
            start = s[j]
            strin += s[j]
            j += 1
        else:
            answer = max(answer, len(strin))
            break

print(answer)
