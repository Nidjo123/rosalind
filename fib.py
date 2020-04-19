
n, k = map(int, input().split())

mem = [1 for _ in range(n)]
for i in range(2, n):
    mem[i] = mem[i - 2] * k + mem[i - 1]

print(mem[n - 1])
