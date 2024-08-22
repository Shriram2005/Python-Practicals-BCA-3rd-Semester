'''
Write a menu-driven program to create mathematical 3D objects I. curve II. sphere III. cone IV. arrow V. ring VI. Cylinder.
'''


import matplotlib.pyplot as plt
import numpy as np


# Function to plot a curve
def plot_curve():
    t = np.linspace(0, 10, 100)
    x = t
    y = np.sin(t)
    z = np.cos(t)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    ax.set_title('3D Curve')
    plt.show()


# Function to plot a sphere
def plot_sphere():
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color='b', alpha=0.6)
    ax.set_title('3D Sphere')
    plt.show()


# Function to plot a cone
def plot_cone():
    phi = np.linspace(0, 2 * np.pi, 100)
    z = np.linspace(0, 10, 100)
    r = z / 2 + 1

    x = r * np.cos(phi)
    y = r * np.sin(phi)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    ax.set_title('3D Cone')
    plt.show()


# Function to plot an arrow
def plot_arrow():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, 1, 1, 1, color='r', label='Arrow')
    ax.set_title('3D Arrow')
    plt.show()


# Function to plot a ring
def plot_ring():
    phi = np.linspace(0, 2 * np.pi, 100)
    x = 5 * np.cos(phi)
    y = 5 * np.sin(phi)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, color='g', label='Ring')
    ax.set_title('2D Ring')
    plt.show()


# Function to plot a cylinder
def plot_cylinder():
    phi = np.linspace(0, 2 * np.pi, 100)
    z = np.linspace(0, 10, 100)

    r = 5
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for zi in z:
        ax.plot(x, y, zi, color='b')

    ax.set_title('3D Cylinder')
    plt.show()


# Main menu
while True:
    print("\n*** 3D Object Creation Menu ***")
    print("1. Curve")
    print("2. Sphere")
    print("3. Cone")
    print("4. Arrow")
    print("5. Ring")
    print("6. Cylinder")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        plot_curve()
    elif choice == '2':
        plot_sphere()
    elif choice == '3':
        plot_cone()
    elif choice == '4':
        plot_arrow()
    elif choice == '5':
        plot_ring()
    elif choice == '6':
        plot_cylinder()
    elif choice == '7':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
