
k, m, n = map(int, input().split())

s = k + m + n
res = 1.0 - n/s*(n-1)/(s-1) - 0.5*m/s*n/(s-1) - 0.5*n/s*m/(s-1) - 0.25*m/s*(m-1)/(s-1)

print(res)
