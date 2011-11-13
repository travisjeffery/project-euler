def fibonacci_sequence_under(boundary):
    x, y = 0, 1
    while x < boundary:
        yield x
        x, y = y, x + y

print sum([i for i in fibonacci_sequence_under(4000000) if i % 2 == 0])
