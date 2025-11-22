n, k, m = map(int, input().split())
a = ((n//k)*m + (n%k)*m)*2
print(a)