s = list(map(lambda x: x*x, [1, 2, 3, 4, 5]))
ss = ' '.join(list(map(str, s)))
print(ss)

f = ss.split()
print(f)
f.reverse()
print(f)