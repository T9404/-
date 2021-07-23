'''
1) Дополнительные фишки питона, которые могут быть полезными
https://pavel-karateev.gitbook.io/intermediate-python/funkcionalnoe-programmirovanie/lambdas

2) Системы СС и о них
https://ege-study.ru/ru/ege/materialy/informatika/zadacha-16-razbor-razlichnyx-tipov-zadach/

'''

#3) Нахождение суммы цифр числа
#summa = sum(map(int, str(input())))

#4) Что такое длина отрезка и количество точек в нем?
#Длина: конец-начало
#Количество: конец-начало+1

#5) В чем разница между ‘is’ и ‘==’ в python

'''
Оператор is сравнивает идентичность двух объектов,
в то время как оператор == сравнивает значения двух объектов.
https://programmera.ru/uroki-po-python/v-chem-raznitsa-mezhdu-is-i-v-python/
'''

list_1 = ['a', 'b', 'c']
list_2 = list_1
list_3 = list(list_1)
print(list_1)
print(list_2)
print(list_3)

print('>>>>> == ')
print(list_1 == list_2)
print(list_1 == list_3)

print('>>>>> is ')
print(list_1 is list_2)
print(list_1 is list_3)



# 6) Find в python
print('>>>> find')
dring = 'gcGC'
print('gcGC'.find(dring)) #если строка состоит из 'gcGC' то выведет индекс найденного элемента, вывел 0

word = 'gcGCgcGCgcGCgcGCfdsfgcGC'
print('gcGC'.find(word)) #вывел -1, т.к. не нашел элемент 

dr = 'gcGC dased gcGC'
print('gcGC'.find(dr)) # вывел -1, т.к. строка состоит не только из одной комбинации gcGC


# 7) Count в python
print('>>>>>> count')
string = '88005553535прощепозвонитьчемукого-тозанимать'
print(string.count('0')) #вернет 2, т.к. два нуля в строке. Лучше не играть с этим в 24 задании в подстроках, т.к. теряет. он проходит через строку, а не через элемент
print(string.count('5')) # вернет 5


# 8) Проверка на простоту
if all(1231 % j!=0 for j in range(2, int(1231**0.5)+1)):
    print('Простое')

def f(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return 'Составное'
    return 'Простое'
print(f(1232))

print('>>>>>>>\nСортировка')
#8) Сортировка в питоне

list_new = [ 2, 213, 41, 414, 1, 1999, 10000, 1, 2, 1]
print(sorted(list_new, key=lambda x: x%2 ))
'''
https://proproprogs.ru/python_base/sortirovka-sort-i-sorted
'''

#9) Использование yield
print('>>>>>Фибоначчи')
def number_range(n): #алгоритм для чисел Фибоначчи
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a+b
data = list(number_range(10000))
print(data[-1])

'''
P.S. рекурсивный метод в питоне может написать: maximum recursion, поэтому пользуйтесь:
import sys
sys.getrecursionlimit(глубина рекурсии)


https://all-python.ru/osnovy/yield.html
'''


print('>>>>>>enumerate')
#10) Питонический цикл
data = [20, 500, 62, 174]
for i, value in enumerate(data, 1): #индекс с 1, а не с нуля!!!
    print(i, value)

try:
    for i, x_value in enumerate(6, 1):
        pass 
except:
    print('\nтак не работает')

print('\n>>>>>>set')
#11 Множества
a = set()
a.add(12)
a.add(1)
print(a)

a_new = {i for i in [9, 8, 9, 8, 7]}
print(a_new) #посмотрите что вернуло
#add, remove, pop, discard(удаление, даже если не сущ элемента)

'''
СМОТРИТЕ на вывод
'''
