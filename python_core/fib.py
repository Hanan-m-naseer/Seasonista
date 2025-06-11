n = 12
fib_series = [0, 1]

for _ in range(n - 2):
    fib_series.append(fib_series[-1] + fib_series[-2])

print("Fibonacci series:", fib_series)
