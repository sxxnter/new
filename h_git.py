def returner(a):
    return a**a

my_list = list(map(returner, [1, 2, 3, 4, 5]))
my_list.reverse()
print(my_list)