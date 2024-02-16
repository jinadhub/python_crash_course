#!/usr/bin/python3 

def count_down(start_number):
    current = start_number
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")

count_down(5)
count_down(0)


