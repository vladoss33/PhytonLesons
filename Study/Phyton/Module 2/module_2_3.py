my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while True:
    if index == len(my_list)-1 or my_list[index] < 0:
        break
    elif my_list[index] > 0:
        print(my_list[index])
    index = index+1