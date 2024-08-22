'''
WAP to find sum of the following series for n terms: 1 – 2/2! + 3/3! - - - - - n/n!
'''

import math

def series_sum(n):
    total = 0
    for i in range(1, n + 1):
        term = ((-1) ** (i - 1)) * (i / math.factorial(i))
        total += term
    return total

n = int(input("Enter the number of terms: "))
result = series_sum(n)
print(f"Sum of the series for {n} terms: {result}")
