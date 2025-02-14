from locale import format_string

input_user = '1234'
number = int(input_user)
ca1 = number // 1000
ca2 = (number % 1000) // 100
ca3 = (number % 100) // 10
ca4 = number % 10
print(ca1)
print(ca2)
print(ca3)
print(ca4)

#2я домашка

input_num = '12345'
ab = int(input_num)
a1 = ab % 10
a2 =  (ab // 10) % 10
a3 = (ab // 100) % 10
a4 = (ab // 1000) % 10
a5 = (ab // 10000) % 10
input_total = f'{a1}{a2}{a3}{a4}{a5}'
print(input_total)



# Additional tasks
text = '''I'm getting better at this!'''
print(text)

#2
y = 87.7e10
z = 87.7e-10

print(y > z)
print('y=', y)
print('z=', z)
# y больше z потому, что y это число 877000000000.0 а z это 0.00000000877

#3

x = "5" + "5"    # ответ 55
y = 5 + 5        # ответ 10
print(x, y)

# нет, потому, что первое это мы сумируем 2 строки, а второе это арифметичское сложение

# 4

x = (1, 2, 3)   #tupple
y = [1, 2, 3]   #list
z = {1, 2, 3}   #set

# z не похож на остальные, так как это set. Мы не можем обратиться
# к первому воторому или третему числу, не можем изменить число а также он удаляет дубликаты
z1 = {1,2,3,3,4,4,5,5}
print(z1)

