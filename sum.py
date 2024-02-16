#!/usr/bin/python3 

def calculate_sum(n):
    sum = 0
    i = 1
    while (i < n):
        print(f"the current value of i is {i}")
        sum += i
        print(f"sum: {sum}")
        i += 1
    print(sum)

calculate_sum(5)



