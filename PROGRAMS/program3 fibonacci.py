'''
WAP to display the first n terms of Fibonacci series.
'''

n = int(input("Enter a number = : "))
a,b,c=0,1,0

while n>0:
    print(c)
    a=b
    b=c
    c=a+b
    n = n -1