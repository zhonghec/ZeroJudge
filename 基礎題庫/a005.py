t = int(input())
for i in range(t):
    a, b, c, d = map(int, input().split())
    if b-a == c-b and c-b == d-c:
        print("{} {} {} {} {}" .format(a, b, c, d, d+c-b))
    else:
        print("{} {} {} {} {}".format(a, b, c, d, d * c // b))