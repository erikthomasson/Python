num=0
start_list = [5, 3, 1, 2, 4]
square_list = []
square_list = start_list

print(square_list)
for i in range(len(square_list)):
    square_list[i] = square_list[i] * square_list[i]
    print(square_list, '\n')


square_list.sort()
print(square_list)