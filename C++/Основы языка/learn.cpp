﻿// Всем привет, этот файл поможет вам в основах С++


// Весь код С++ работает в функции int main() {}, если вы не создадите подобный функции- вы получите ошибку и не сможете запустить код
// Как любая функция типа int, на выходе требует возвращение значения(в отличии от void), если вернуло 0, успешно, иначе- где-то произ. ошибка

/* 
int main() {
	std::cout<<"Hello world";
	return 0;
}
*/




// I) Библиотеки


#include <iostream> // подключение библиотеки ввода-вывода(input-output)

/* 
Здесь будут пополняться встроенные библиотеки, необходимые для КЕГЭ
*/


/*
Существуют два режима конфигурации(как бы запуска программы)
1) Debug - с нее помощью можно отлаживать код, при этом создаваемый файл больше и медленнее
2) Release - по названию понятно. Когда прога прошла все тесты, ее можно оптимизировать

Я думаю, мы будем почти всегда пользоваться Debug, возможно за иск. 27х задач

*/




// II) Инициализация и присваивание


/*
Переменные в С++ требуют своего типа до начала работы с ними, т.к. иначе компилятор не сможет работать

int a;  - инициализация
int a_1 = 21; - инициализация с присваиванием



int i=10
float j=5;
float b;
b=i+j; // сработает

*/


/*
Основные типы данных в C++
int (целый);
char (символьный);
wchar_t (расширенный символьный);
bool (логический);
float (вещественный);
double (вещественный с двойной точностью).
long int;
short int;
*/



// III) Ввод-вывод
/*
Все очень просто, подключите библиотеку iostream и работайте

cin - ввод, cout - вывод, endl - перенос на след строку

#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;
    return 0;
}
*/


// III.2) Циклы
/*
for, while, do-while

int a = 2;
do {
cout << "HI, people!";
} while (a < 1);
Что получаем? Цикл do-while ВСЕГДА выполняется, затем заходит в условие, если не удв- выходит

i++  это тоже, что и  (i = i + 1) || (i+=1)

*/


//  IV) Закрывается консоль. Помогите!

/*
1) 
Написать 
system("pause");

2) Ввод данных и ожидание программы
int a;
cin >> a;


3) 
Функция getch нужна для чтения одного символа с клавиатуры, этот символ на экран не выводится
Мы как бы держим консоль, чтобы она не закрывалась
Нужно подключать библиотеку)

#include <conio.h>

#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << a + b;

    getch(); // ждет, пока вы не нажмете любую клавишу
    // нажимаем
    return 0; // выполняется
}

*/


// V) Математические функции
/*
#include <cmath>  // подключение библиотеки 

pow(a, b); - возведем a в степень b | a**b
sqrt(a); - найдем квадратный корень из числа а | a**0.5

round(2.5); - округлит в 3
round(2.4); - округлит в 2, Т.Е. округляет согласно математике

ceil(2.3); - округлит в 3 (большую сторону)
floor(2.99); - округлит в 2 (меньшую сторону)

*/

// VI) Условные операторы:
/*
if; else if; else; switc-case;

#include <iostream>
using namespace std;


int main() {
	int num =   1 == 1 ? 12 : 23; // если 1 == 1, то num = 12; иначе num=23;

		if (num > 12) {
		return true; 
		} else if (num == 12) {
		cout << "Num is 12";
		} else {
		return false;}


	switch (num) {
		case 1:
			cout << "Num is 1";
		case 12:
			cout << "Num is 12" << endl;
		case 13:
			cout << "Num is 13";
		default: // можно не писать, в случае если ничего не выполнится- выполнится default
			cout << "I dont know";
		}
	return 0; 
}
*/



// VII) Массивы. Хранение данных

/* 
как работать? можно подключить библиотеку, когда это надо
#include <vector>

0) Объявление массива
double arr[4];

1)
string students[10] = {    // 10 - кол-во элементов в массиве
	 "Иванов", "Петров", "Сидоров",
        "Ахмедов", "Ерошкин", "Выхин",
        "Андеев", "Вин Дизель", "Картошкин", "Вандель"
}
std::cout << students <<std::endl; // посмотрите вывод

//Если мы объявляем переменную типа int, то на машинном уровне она описывается двумя параметрами — ее адресом и размером хранимых данных.
// выводим все через цикл и тренируем  их)))



2)
//ввод
int array[4][2] = { {444, 12}, {124, 41}, {312, 433}, {234, 999} };
array[0][0] = 23;

//вывод
for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 2; j++)
			cout << array[i][j] << endl;
	}



3) // массив без инициализации
bool good_or_false[2]; 



4) // заполнение массива

int arr[10];

	// Заполняем массив с клавиатуры
	for (int i = 0; i < 10; i++) {
		cout << "[" << i + 1 << "]" << ": ";
		cin >> arr[i];
	}

	// И выводим заполненный массив.
	cout << "\nYour array: ";

	for (int i = 0; i < 10; ++i) {
		cout << arr[i] << " ";
	}



*/


// IX) Указатели. Память)
/*
Оператор адреса & позволяет узнать, какой адрес памяти был присвоен переменной
Оператор разыменования * позволяет получить значение по указанному адресу:
int a = 12;
&a - выведет 0043CCF0 наподобие
*&a - выведет 12

Зачем они вообще нужны? Для работы с динам. памятью
*/

// X) Динамические массивы

/*
Создали элемент динамичный- не забудьте его удалить!

void main() {
	int size = 0;
	cout << "what";
	cin >> size;
	int  *arr = new int[size]; //если вы используете двумерный массив, у вас 2 массива => две звезды. **arr = new int[size];

	for (int i = 0; i < size; i++) {
		arr[i] = rand() % 10;
	}

	for (int i = 0; i < size; i++) {
		cout << arr[i] << "\t";

		cout << arr+i << endl;
	}


	delete[] arr;
}

Чтобы удалить двумерный массив:
for (int i = 0, i < скок всего подмассивов; i++) {
	delete [] arr[i];
}
delete[] arr; -удаление большого массива

*/




// P.S. Прикольные штуки
/*
1) БЕсконЕчность
double zero = 0.0;
double posinf = 5.0 / zero; // если отриц бесконечность, то -5.0 / zero
cout << posinf << "\n";

2) Как в С++ поменять элементы местами? С помощью swap;
int a = 12; int b = 123;
swap(a, b);

3) СОВЕТ: Пользуйтесь отладкой, помогает. 
Нажмите на нужную строку(красным загорится). Выберите тип отладка. я использую F10. Работайте)

4) Встроенная сортировка с предикатом + лямбда выражение
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
		vector<int> v = { 9, 12, 3, 121, 41, 1 };
		sort(v.begin(), v.end(), [](int a, int b) {
			return a > b;
});

5) Проблемы с русским языком, решение:
setlocale(LC_ALL, "ru");

6) sizeof(элемент) -возвращает объем занимаемой памяти массива
Как узнать длину массива?
sizeoff(arr)/sizeoff(int); // массив с int числами, делим на 1 элемент
*/