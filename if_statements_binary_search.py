v0: int = 20000000000000000
v1: int = 0
v2: int = v0
while v1 != v2:
    if (v2 - v1) % 2 == 0:
        v3 = v1 + (v2 - v1) // 2
    else:
        v3 = v1 + (v2 - v1) // 2 + 1

    if v3 * v3 > v0:
        v2 = v3 - 1
    else:
        v1 = v3
print(f'sr({v0}) = {v1}')
