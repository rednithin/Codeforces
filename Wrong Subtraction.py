# https://codeforces.com/problemset/problem/977/A

n, k = [int(x) for x in input().split(' ')]

while k != 0:
    if n % 10 == 0:
        n //= 10
    else:
        n -= 1
    k -= 1

print(n)
