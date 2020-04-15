t = int(input())

while t != 0:
    a, b, c = [int(x) for x in input().split(' ')]
    while b != 0 and a > 20:
        a = a // 2 + 10
        b -= 1
    a -= c * 10
    if a > 0:
        print("NO")
    else:
        print("YES")
    t -= 1
