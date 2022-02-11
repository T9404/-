'''
Что нужно знать?
and ----> ∧
or  ----> v
→   ----> <=  P.S. подумайте почему
=   ----> ==
≠   ----> !=
'''

print('>>>>>>>')

#К.Ю.Поляков 385 
'''
 Элементами множеств А, P, Q являются натуральные числа, причём P={1,3,7},
 Q={1,2,4,5,6}. Известно, что выражение

((x ∉ A) → (x ∉ P)) ∨ ((x ∉ Q) ∧ (x ∈ P))
истинно (т.е. принимает значение 1 при любом значении переменной х.
Определите наименьшее возможное количество элементов в множестве A. 
'''

p = {1, 3, 7}
q = {1, 2, 4, 5, 6}

def f(x, a):
     return  ((x not in  a) <= (x not in p)) or ((x not in q) and (x in p))

a = set()   #если найти наименьшее, то мы ничего не делаем и прибавляем 'x' по необходимости
for x in range(1, 1000):
    if not f(x, a):
        a.add(x)
        
print(sorted(a))



print('>>>>>>>')
#К.Ю.Поляков 3434 https://prnt.sc/1aib15w
'''
Элементами множеств А, P и Q являются натуральные числа, причём 
P={2, 4, 6, 8, 10, 12, 14, 16, 18, 20}  и Q={5, 10, 15, 20, 25, 30, 35, 40, 45, 50}. 
Известно, что выражение
((x ∈ A) → (x ∈ P)) ∨ (¬(x ∈ Q) → ¬(x ∈ A))
истинно (т.е. принимает значение 1 при любом значении переменной х. 
Определите наибольшее возможное количество элементов в множестве A. 
'''

P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}

A = set(range(1, 1000)) # 0 не берем! (не натуральное). Определите наибольшее - делаем A изначально большим
for x in range(1, 1000):
    if not ( ((x in A) <= (x in P)) or (not(x in Q) <= (not(x in A))) ):
        A.remove(x) # удаляем, если не выполняется при определенном X. 
print(len(A))




'''
Это 2 подтипа из типа задач №15. Решайте руками и программой. Но если вы ленивый программист,
то можно только последнее)
'''
