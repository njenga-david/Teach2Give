#Write a program that generates a fibonacci sequence upto 100
def fibonacci_sequence():
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= 100:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print(fibonacci_sequence())
