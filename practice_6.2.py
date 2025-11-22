A,B = map(int,input().split("x")) # Стена
a = []
a.append(A)
a.append(B)
C,D,E = map(int,input().split("x"))# rbhgbx
c = []
c.append(C)
c.append(D)
c.append(E)
a = sorted(a)
c = sorted(c)

if c[0] <= a[0] and c[1] <= a[1]:
    print("да")
else:
    print("нет")


