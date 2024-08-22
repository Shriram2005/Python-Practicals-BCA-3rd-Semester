'''
WAP to read n integers and display them as a histogram
'''

def histogram(items):
    for n in items:
        output = ''
        times = n
        while times > 0:
            output += '*'
            times = times - 1
        print(output)

histogram([2, 3, 6, 5])