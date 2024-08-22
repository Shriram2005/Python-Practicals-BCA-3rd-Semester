'''
WAP to calculate the sum and product of two compatible matrices.
'''
X = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

Y = [[5, 8, 1],
    [6, 7, 3],
    [4, 5, 9]]

add =[[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]] 

multiply = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
       add[i][j] = X[i][j] + Y[i][j]
       multiply[i][j] = X[i][j] * Y[i][j]

print("\nSum of Matrices (X + Y):")
for r in add:
    print(r)

print("\nProduct of Matrices (X * Y):")
for i in multiply:
    print(i)
