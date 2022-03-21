'''
Что нужно знать?
and ----> ∧
or  ----> v
→   ----> <=  P.S. подумайте почему
=   ----> ==
≠   ----> !=
'''


''' 
Это очень важно! 
https://inf-ege.sdamgia.ru/problem?id=11119
'''




print('>>>>>>')
# К.Ю.Поляков 367
'''
На числовой прямой даны два отрезка: P=[37,60] и Q=[40,77]. 
Укажите наименьшую возможную длину такого отрезка A, что формула
(x ∈ P) → (((x ∈ Q) ∧ (x ∉ A)) → (x ∉ P))
тождественно истинна, то есть принимает значение 1 при любом значении переменной х. 
'''


def f(x, a1, a2):
    return (37 <= x <= 60) <= (((40 <= x <= 77) and (not (a1 <= x <= a2))) <= (not (37 <= x <= 60)))


m = float('inf')

for a1 in range(35, 80):
    for a2 in range(a1, 80):  # Каждый раз мы создаем новый отрезок и пропускаем его через функцию

        if all(f(x, a1, a2) == 1 for x in range(1, 1000)):
            if a2-a1 < m:
                m = a2-a1
                start = a1
                end = a2

# рисуйте ось и отметьте все точки ( 37, 40, 60, 77 ), ответ: 60-40
print(start, end)
print(m)









print('>>>>>>')
# К.Ю.Поляков 362
'''
На числовой прямой даны два отрезка: P=[2,10] и Q=[6,14]. 
Какова максимальная длина отрезка A, при выборе которого формула
((x ∈ А) → (x ∈ P)) ∨ (x ∈ Q)
тождественно истинна, то есть принимает значение 1 при любом значении переменной х. 
'''


def f(x, a1, a2):
    return ((a1 <= x <= a2) <= (2 <= x <= 10)) or (6 <= x <= 14)


m = 0

for a1 in range(2, 15):
    for a2 in range(a1, 15):
        if all(f(x, a1, a2) == 1 for x in range(1, 1000)):
            if a2-a1 > m:
                m = a2-a1
                start = a1
                end = a2


print(start, end)
print(m)  # рисуйте ось и отметьте все точки: 2, 6, 10, 14; ответ: 14 - 2 = 12




'''
Длина: конец-начало
Количество: конец-начало+1
'''
