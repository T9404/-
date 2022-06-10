'''
Исполнитель Редактор получает на вход строку цифр и преобразовывает её. 
Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки символов.
1. заменить (v, w) 
2. нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. 
Если цепочки v в строке нет, эта команда не изменяет строку. Вторая команда проверяет, 
встречается ли цепочка v в строке исполнителя Редактор.
Дана программа для исполнителя Редактор:
НАЧАЛО
ПОКА нашлось(111) или нашлось(333)
  ЕСЛИ нашлось(111) 
  ТО заменить(111, 3)
  ИНАЧЕ заменить(333, 1)
КОНЕЦ ПОКА
КОНЕЦ
На вход программе подана строка из более чем 100 подряд идущих символов «3». Найдите 
минимальную длину входной строки, в результате обработки которой получится 
минимальное возможное число.
'''
# https://prnt.sc/vipoM--lZ4Rq


min_numb = float('inf')


for i in range(101, 120):
    s = '3' * i

    while '111' in s or '333' in s:
        if '111' in s:
            s = s.replace('111', '3', 1)
        else:
            s = s.replace('333', '1', 1)

    if min_numb > sum(map(int, s)):
        min_numb = sum(map(int, s))
        j = i


print(j)
