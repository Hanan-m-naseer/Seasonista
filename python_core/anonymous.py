#task40

sub = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_sub = sorted(sub, key=lambda x: x[1])

print("Sorted list of tuples:", sorted_sub)

#task41
devices = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

sorted_devices = sorted(devices, key=lambda x: int(x['model']))

print("Sorted list of dictionaries:", sorted_devices)

#task42
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


squared_numbers = list(map(lambda x: x**2, numbers))
cubed_numbers = list(map(lambda x: x**3, numbers))


print("Squared numbers:", squared_numbers)
print("Cubed numbers:", cubed_numbers)

#task43
from functools import reduce

fibonacci_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1]) 

n = 10  
fib = fibonacci_series(n)
print("Fibonacci series up to", n, ":", fib)


#task44
numbers = list(range(1, 50)) 

divisible_numbers = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))

print("Numbers divisible by 19 or 13:", divisible_numbers)

#task45
numbers=[-1,4,-5,6,-2]

sum = reduce(lambda s,x: s+x,numbers)
print("Total sum of numbers:", sum)

