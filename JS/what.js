/**
 * Как посмотреть вывод?
 * 1)Запустите в браузере index.html
 * 2) Нажмите на ПКМ
 * 3) Просмотреть код
 * 4) Console 
 * 5) https://prnt.sc/1ajm7q4
 */

/** К.Ю.Поляков  ТИП №17 Номер 4052  
 * Рассматривается множество целых чисел, принадлежащих числовому отрезку [5913; 11753],
 * которые делятся на 5 и 11 и не делятся на 7, 10, 13, 22. Найдите количество таких чисел и минимальное из них. 
 * В ответе запишите два целых числа: сначала количество, затем минимальное число. 
 */

 let mina = 100000000000000;
 let count = 0;
 for (let i=5913; i<11753; i++) 
 {
     if ( (i % 5 === 0) & (i % 11 ===0) & (i % 7 !== 0) & (i % 10 !== 0) & (i % 13 !== 0) & (i % 22 !== 0)) {
       count+=1;
       mina = Math.min(i, mina);
 
     };
 };
 console.log(count);
 console.log(mina);
 
 
 
 
 // К.Ю.Поляков ТИП№ 25 Номер 3977
 /**
  * Найдите все натуральные числа, N, принадлежащие отрезку [150 000 000; 300 000 000], которые можно представить в виде N = 2m•3n,
  *  где m – чётное число, n – нечётное число. В ответе запишите все найденные числа в порядке возрастания, а справа от каждого числа – сумму m+n. 
  */
 

 
 let answer = []; 
 
 for (let m=2; m<29; m+=2 ) {
     for (let n=1; n<30; n+=2) {
 
         let num = (2**m)*(3**n);
 
         if ( num >= 150000000 && 300000000 >= num ) {
             answer.push(num);
             answer.push(n+m);
             //console.log( (2**m)*(3**n));
             //console.log(m+n);
             //console.log('good');
 
             //console.log(m+n);
 
         
             } else {
                 continue;
             };
         };
     };
 
 console.log(answer);
 
 
 