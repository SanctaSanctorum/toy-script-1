hand = open("styles.css")
counts = dict()
for line in hand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print([k,v = counts.item()])
lis = list()
for k, v in counts.items():
    lis.append((v,k))
lis = sorted(lis, reverse=True)

for v, k in lis[:10]:
    print(k, v)

value = [1, 2, 3, 4, 5]
print(value[2])
