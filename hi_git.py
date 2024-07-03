def returner(a):
    return a**a

print(list(map(returner, [1, 2, 3, 4, 5])))