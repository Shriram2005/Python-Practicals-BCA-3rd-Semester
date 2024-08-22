'''
WAP to plot a graph of people with pulse rate p vs. height h. The values of p and h are to be entered by the user
'''


import matplotlib.pyplot as plt

def plot_pulse_rate_vs_height():
    num_people = int(input("Enter the number of people: "))

    heights = []
    pulse_rates = []

    for i in range(num_people):
        height = float(input(f"Enter height for person {i + 1} (in cm): "))
        pulse_rate = int(input(f"Enter pulse rate for person {i + 1} (in bpm): "))

        heights.append(height)
        pulse_rates.append(pulse_rate)

    # Plotting the graph
    plt.scatter(heights, pulse_rates, color='blue', marker='o')
    plt.title('Pulse Rate vs. Height')
    plt.xlabel('Height (cm)')
    plt.ylabel('Pulse Rate (bpm)')
    plt.grid(True)
    plt.show()

# Call the function to plot the graph
plot_pulse_rate_vs_height()
