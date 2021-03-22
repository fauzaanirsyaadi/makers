def circularArrayRotation(a, k, queries):
    result= [-1]*(len(a))
    for i in range(len(a)):
        moveTo = (i+k)%len(a)
        result[moveTo] = a[i]
    return [result[q] for q in queries]
a= [1,2,3]
k = 2
q = [0,1,3]
print(circularArrayRotation(a, k, q))
