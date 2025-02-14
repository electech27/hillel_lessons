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

input_num = '12345'
ab = int(input_num)
a1 = ab % 10
a2 =  (ab // 10) % 10
a3 = (ab // 100) % 10
a4 = (ab // 1000) % 10
a5 = (ab // 10000) % 10
print(a1, a2, a3, a4, a5)
