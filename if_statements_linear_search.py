v0: int = 100
for i in range(v0):
    if i * i > v0:
        v1 = i - 1
        break
print(f'sr({v0}) = {v1}')
