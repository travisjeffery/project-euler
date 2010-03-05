from gauss import fib

i = 1
while 1:
    if len(str(fib(i))) >= 1000:
        print i
        break
    else:
        i += 1