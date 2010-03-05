from math import factorial

def perms(n):
    answer = ''
    digits = [0,1,2,3,4,5,6,7,8,9]
    for i in xrange(9, -1, -1):
        fact = factorial(i)
        digit = (n-1)/fact
        answer += str(digits.pop(digit))
        n -= digit * fact
    return answer

print perms(1000000)
