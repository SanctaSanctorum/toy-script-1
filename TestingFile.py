dic = {'m': 10, 'n': 3, 's': 15}
lis = list()
for k, v in dic.items():
    lis.append((v, k))
lis = sorted(lis, reverse=True)
print(lis)