def print_fibonacci(length):
    #initialize two numbers of the fs
    
    f_s=[0,1]
    # generate to a length
    while len(f_s)<length:
        next_num=f_s[-1]+f_s[-2]
        f_s.append(next_num)
        print('fibonacci sequence')
    for num in f_s:
        print(num, end="")
        print()
print_fibonacci(10)