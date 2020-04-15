from pprint import pprint
from collections import defaultdict

n, k = [int(x) for x in input().split(' ')]
arr = [[] for _ in range(n + 2)]
t = n - 1


while t != 0:
    a, b = [int(x) for x in input().split(' ')]
    arr[a].append(b)
    arr[b].append(a)
    t -= 1


b = 0


def calc_paths(start, ):
    if(len(arr[start]) == 0):
        return 1
