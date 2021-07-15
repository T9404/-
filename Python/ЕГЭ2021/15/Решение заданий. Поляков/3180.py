print('>>>>>>>>>')
#3180 К.Ю.Поляков
'''
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». 
Для какого наибольшего натурального числа A формула
ДЕЛ(70, A) ∧ (¬ДЕЛ(x, A) → (ДЕЛ(x, 35) → ¬ДЕЛ(x, 63)))
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)? 
'''
def f(a, x):
    return  (70 % a == 0) and ((x % a != 0) <= ((x % 35 == 0) <= (x % 63 != 0)))

for a in range(5000, 1, -1):
    flag = True #P.S. Всегда ставьте значения сначала на True или один
    for x in range(1, 10000):
        if not f(a, x):
            flag = False
            break
    if flag:
        print(a)
        break
