# linegraphs.py

import matplotlib.pyplot as plt
import numpy as np

def two_linegraphs(func1, func2, range, steps):
    """
    Plot a 3D line graph of two parametric functions.
    """
    
    # Define the parameter t to be in range, give it appropriate no. of steps
    t1 = np.linspace(range[0], range[1], steps)
    t2 = np.linspace(range[0], range[1], steps)

    # Match each function to corresponding parameter in "t"
    # Define two sets of variables
    x_1, y_1, z_1 = zip(*[func1(ti) for ti in t1])
    x_2, y_2, z_2 = zip(*[func2(ti) for ti in t2])
    
    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    # Plot the line & make a legend that displays the function
    ax.plot(x_1, y_1, z_1, color='r', label="Function 1")
    ax.plot(x_2, y_2, z_2, color='blue', label="Function 2")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_zlabel("z-axis")
    ax.legend()
    plt.title("Function 1 vs. Function 2")
    plt.show()