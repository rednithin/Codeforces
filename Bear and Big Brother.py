# https://codeforces.com/problemset/problem/791/A

a, b = [int(x) for x in input().split(' ')]

count = 0

while a <= b:
    a = 3 * a
    b = 2 * b
    count += 1

print(count)
