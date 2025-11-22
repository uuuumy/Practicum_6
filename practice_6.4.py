n = int(input())
n1 = int(n[0])
n2 = n[1]
n2 = n2.replace("a", 1)
n2 = n2.replace("b", 2)
n2 = n2.replace("c", 3)
n2 = n2.replace("d", 4)
n2 = n2.replace("e", 5)
n2 = n2.replace("f", 6)
n2 = n2.replace("g", 7)
n2 = n2.replace("h", 8)
if (n1 + n2) % 2 == 0:
    print("Черная")
else:
    print("Белая")
