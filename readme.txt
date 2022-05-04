A Road consists of units: "." means a good condition and "o" means a hole. There is a machine (X units in length) that can fix holes along a road. The machine has the Section which can fix X holes in a time. The goal is to process a road of length N to fix all holes with the fewest possible iterations that are done by the machine.
Example 1 if X=3: A road represented by ".o." would require 1 fix.
Example 2 if X=3: A road represented by "..o...o" would require 2 fixes.
Example 3 if X=3: A road represented by "ooo.oooo" would require 3 fixes.
Example 4 if X=3: A road represented by ".o.oo.oo.o" would require 3 fixes.

Your task is to write a program that takes a string representing a road and returns the smallest number of fixes that will remove the holes.

It would be nice to add S which will represent the number of holes that can be skipped to have better performance over quality.
Example 5 if S = 1 AND X=3: A road represented by "ooo.oooo" would require 2 fixes.

****************

Дорога складається з одиниць: "." означає гарний стан, а «о» означає отвір. Є машина (X одиниць довжини), яка може виправляти діри вздовж дороги. Машина має секцію, яка може виправити X отворів за один раз. Мета полягає в тому, щоб обробити дорогу довжиною N, щоб зафіксувати всі отвори з якомога меншою кількістю ітерацій, які виконує машина.
Приклад 1, якщо X=3: дорога, представлена символом ".o." вимагатиме 1 виправлення.
Приклад 2, якщо X=3: дорога, представлена символом "..o...o", потребує 2 виправлень.
Приклад 3, якщо X=3: дорога, представлена "ooo.oooo", потребує 3 виправлень.
Приклад 4, якщо X=3: дорога, представлена ".o.oo.oo.o", потребує 3 виправлень.

Ваше завдання — написати програму, яка бере рядок, що представляє дорогу, і повертає найменшу кількість виправлень, які видаляють діри.

Було б непогано додати S, який представлятиме кількість отворів, які можна пропустити, щоб мати кращу продуктивність над якістю.
Приклад 5, якщо S = 1 І X=3: Дорога, представлена символом "ooo.oooo", потребує 2 виправлень.