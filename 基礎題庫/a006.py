import math
a, b, c = map(int, input().split())
if b*b - 4*a*c < 0: print("No real root")
else:
    d = math.sqrt(b * b - 4 * a * c)
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    if x1 == x2:
        print("Two same roots x=%d" %x1)
    elif x1 > x2:
        print("Two different roots x1=%d , x2=%d" %(x1, x2))
    else: print("Two different roots x1=%d , x2=%d" %(x2, x1))