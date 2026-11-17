l1 = []
for i in range(1,31):
    l1.append(i)
l2 = [i for i in l1 if i % 2 == 0]
print(l2)