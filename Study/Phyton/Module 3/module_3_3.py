def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(2, 'Пельмени')
print_params(b='Абадон', c=False)
print_params(a=9, c=False)
print_params()

print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [2.5, (1, 2, 3), 'Rofls']
values_dict = {'a': 100, 'b': 'Три', 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [5, 6]

print_params(*values_list_2, 42)