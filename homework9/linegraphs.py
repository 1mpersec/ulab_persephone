# linegraphs.py

import matplotlib.pyplot as plt
import numpy as np

def two_linegraphs(func1, func2, range, steps):
    """
    Plot a 3D line graph of two parametric functions on the same axes.
    Define parameter "t" through the given range and no. of steps.
    """
    
    # Define the parameter t to be in range, give it appropriate no. of steps
    t = np.linspace(range[0], range[1], steps)

    """
    Using zip allows us to receive x, y, z values by attributing one
    parameter (ti) out of the list (t) that was created with np.linspace.
    """
    # Match each function to corresponding parameter in "t"
    # Define two sets of variables
    x_1, y_1, z_1 = zip(*[func1(ti) for ti in t])
    x_2, y_2, z_2 = zip(*[func2(ti) for ti in t])
    
    # Create figure in 3D
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    # Plot the line & make a legend that displays the function
    ax.plot(x_1, y_1, z_1, color='r', label="Function 1")
    ax.plot(x_2, y_2, z_2, color='blue', label="Function 2")
    ax.legend()

    # Label the x, y, z axes
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_zlabel("z-axis")

    # Give the graph a title
    plt.title("Function 1 vs. Function 2")

    # Display the final product
    plt.show()