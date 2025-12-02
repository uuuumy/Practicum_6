n, m = map(int, input().split("x"))
k = int(input())

if k < n * m and (k % n == 0 or k % m == 0):
    print("Успешно")
else:
    print("Неосуществимо")
