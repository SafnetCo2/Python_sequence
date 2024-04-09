def print_fibonacci(length):
    fibonacci_sequence=[0,1]
    while len(fibonacci_sequence)<length:
        next_num=fibonacci_sequence[-1]+fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    print('Fibonacci sequence')
    for num in fibonacci_sequence:
        print(num, end=" ")
print_fibonacci(10)
    