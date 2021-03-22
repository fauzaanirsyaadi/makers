# https://www.hackerrank.com/challenges/30-conditional-statements/problem

N = int(input('input integer: '))
if N % 2 != 0:
    print('Weird')
elif N % 2 ==0 and ( N >=2 and N <= 5):
    print('Not Weird')
elif N % 2 == 0 and (N >= 6 and N <= 20):
    print('Weird')
elif N % 2 == 0 and N > 20:
    print('Not Weird')
