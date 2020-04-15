t = int(input())

while t != 0:
    input()

    red_weights = [(int(x), int(x) ** 2) for x in input().split(' ')]
    green_weights = [(int(x), int(x) ** 2) for x in input().split(' ')]
    blue_weights = [(int(x), int(x) ** 2) for x in input().split(' ')]

    first_weights, second_weights, third_weights = sorted([
        red_weights, green_weights, blue_weights], key=lambda x: len(x), reverse=True)

    k = float('inf')

    for x, xs in red_weights:
        for y, ys in green_weights:
            other = xs + ys - x * y
            for z, zs in blue_weights:
                ans = other + zs - x * z - y * z
                k = min(ans, k)
    print(2 * k)
    t -= 1
