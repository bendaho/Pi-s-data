print('''
Здравствуйте!
Вас приветствует программа определения местонахождения Вашей даты в числе Пи после запятой
''')
print()
a = input('Ведите число, месяц год рождения в формате ччммгг: \n')
f = open("pi-billion.txt", "r")
n = 0
while n < 1000000000:
  k = f.seek(n)
  z = f.read(6)
  n =  n + 1
  # print(n, z)
  if z == a:
    print()
    print(f'Дата Вашего дня рождения встречается на {n-2}-м месте после запятой в числе Пи')
    break by
