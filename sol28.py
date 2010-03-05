import sys

def sol28(prev, interval):
    totl = 0
    if prev == 1:
        totl += 1
    while 1:
        if prev == 1001**2:
            return totl
        for i in range(1, 5):
            totl += prev+(i*interval)
        prev += 4*interval
        interval += 2

print sol28(1, 2)