int1 = int(input("Enter a number: "))
int2 = int(input("Enter a number: "))
int3 = int(input("Enter a number: "))

biggest_num = int1

if int2 > biggest_num: biggest_num = int2
if int3 > biggest_num: biggest_num = int3

print('biggest_num = ', biggest_num)
