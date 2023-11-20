x = int(input())
y = int(input())
def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y
    while True:
        if z % x == 0 and z % y == 0:
            return z
            break
        z += 1

print(lcm(x, y))