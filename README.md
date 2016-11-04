# bda_yandex_test
The program for aprove the test for a big data analityc in Yandex.
https://yandex.ru/jobs/vacancies/analytics/bigdatan_msk
The task  is
"
Каждый день аналитик Петров по пути на работу переходит улицу по пешеходному переходу со светофором. Светофор работает в таком режиме: красный - 75 сек., зеленый - 20 сек. Сколько секунд в среднем Петров стоит на светофоре?
"
This task is possible tosolve with just statistic methods of math. Buuuut ammm
Whell, statistic knows nothing about days off. And the symple statistics solving method does not count
24-hours drift of light sqeuence.
So i've writen a script in python(first time of python scripting) to cunt that things.
How to use it: 
$python3 petrov5.py <year in 4-digit style> <any text or write test>
Year parameter is for counting leap year days, second paramets might be "test" - to check
the first rount of lights drift sequence. If you don't want to use the test option, just type any text as the second parameter.
