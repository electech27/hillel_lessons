first_list = [0,1,0,12,3]
print(first_list[1:2] + first_list[3:] + first_list[:1] + first_list[2:3])

second_list = [0]


print(second_list[1:0] + second_list) #Здесь будет лишним second_list[1:0] так как просто можно оставить print(second_list)



third_list = [1, 0, 13, 0, 0, 0, 5]
print(third_list[0:3:2] + third_list[6:] + third_list[1:2] + third_list[3:6:1])

four_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
four_1 = four_list[0:3:2] + four_list[3:10:2] + four_list[12:13]
four_2 = four_list[1:5:3] + four_list[6:11:2] + four_list[11::2]
print(four_1 + four_2)
