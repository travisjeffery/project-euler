def prodispalindrome(n1, n2):
    n = n1 * n2
    return str(n) == str(n)[::-1]


def palindrome(n):
    return str(n)[::-1]

def maxpalindrome():
    for i in reversed(xrange(100,999)):
        for j in reversed(xrange(100,999)):
            if prodispalindrome(i, j):
                yield i * j

print max(maxpalindrome())
