from itertools import *
print('>>>>>>')
# №3538 К.Ю.Поляков
'''
Все 4-буквенные слова, составленные из букв П, Р, В, Д, А, записаны в алфавитном порядке и пронумерованы. 
Вот начало списка:
1. АААА 
2. АААВ 
3. АААД
4. АААП
5. АААР
6. ААВА
...
Найдите номер первого слова в этом списке, которое не содержит гласных и !одинаковых! - set букв. 
'''
write = 'АВДПР' # !!!!!!!!!!!!!!!! В этом задании важен порядок кодировки символов, А-1, В-2, Д-3, П-4, Р-5
for i, word_i in enumerate(product(write, repeat=4)):
    u = ''.join(word_i)
    if len(set(u)) == 4 and 'А' not in u:
        print(u, i+1)
        break