def savethe(n, m, s):
    b = []
    for i in range(0, m):
        if s !=n:
            b.append(s)
            s = s+1
        elif s == n:
            b.append(s)
            s = 1
    return b[-1]
print(savethe(4, 10, 2))