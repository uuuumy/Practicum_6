k = int(input())

can = False
for i in range(k // 5 + 1):
    for j in range(k // 7 + 1):
        if (5*i + 7*j) == k:
            can = True

if can:
    print("Да")
else:
    print("Нет")
