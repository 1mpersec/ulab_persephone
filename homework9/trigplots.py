#trigplots.py
import numpy as np
import matplotlib.pyplot as plt


def trig_plots_horizontal():
    # Define the domain from 0 to 2π
    x = np.linspace(0, 2 * np.pi, 500)
    
    # Define functions h(x) and k(x) 
    h_x = np.cos(x)
    k_x = np.sin(x)
    
    # Create a figure and two subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns
    
    # Left subplot
    axs[0].plot(x, h_x, label=r"$h(x) = \cos(x)$", color='blue')
    axs[0].set_title(r"$h(x) = \cos(x)$")
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("h(x)")
    axs[0].legend()
    
    # Right subplot
    axs[1].plot(x, k_x, label=r"$k(x) = \sin(x)$", color='green')
    axs[1].set_title(r"$k(x) = \sin(x)$")
    axs[1].set_xlabel("x")
    axs[1].set_ylabel("k(x)")
    axs[1].legend()
    
    # Set the domain for both subplots
    axs[0].set_xlim(0, 2 * np.pi)
    axs[1].set_xlim(0, 2 * np.pi)
    
    plt.show()


def trig_plots_vertical():
    # Define the domain
    x = np.linspace(0, 2 * np.pi, 500)
    
    # Define the functions
    h_x = np.cos(x)
    k_x = np.sin(x)
    
    # Create a figure and two subplots
    fig, axs = plt.subplots(2, 1, figsize=(12, 6))  # 2 rows, 1 column
    
    # Top subplot
    axs[0].plot(x, h_x, label=r"$h(x) = \cos(x)$", color='blue')
    axs[0].set_title(r"$h(x) = \cos(x)$")
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("h(x)")
    axs[0].legend()
    
    # Bottom subplot
    axs[1].plot(x, k_x, label=r"$k(x) = \sin(x)$", color='green')
    axs[1].set_title(r"$k(x) = \sin(x)$")
    axs[1].set_xlabel("x")
    axs[1].set_ylabel("k(x)")
    axs[1].legend()
    
    # Set the domain for both subplots
    axs[0].set_xlim(0, 2 * np.pi)
    axs[1].set_xlim(0, 2 * np.pi)
        
    # Adjust layout so labels don't overlap
    plt.tight_layout()
    
    plt.show()



def expanded_domain_horizontal():
    # Define variable x
    x = np.linspace(0, 2 * np.pi, 500)
    
    # Define functions
    h_x = np.cos(x)
    k_x = np.sin(x)
    
    # Create a figure and two subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns
    
    # Left subplot
    axs[0].plot(x, h_x, label=r"$h(x) = \cos(x)$", color='blue')
    axs[0].set_title(r"$h(x) = \cos(x)$")
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("h(x)")
    axs[0].legend()
    
    # Right subplot
    axs[1].plot(x, k_x, label=r"$k(x) = \sin(x)$", color='green')
    axs[1].set_title(r"$k(x) = \sin(x)$")
    axs[1].set_xlabel("x")
    axs[1].set_ylabel("k(x)")
    axs[1].legend()
    
    # Set domain from 0 to 4π
    axs[0].set_xlim(0, 4 * np.pi)
    axs[1].set_xlim(0, 4 * np.pi)
    
    plt.show()


def expanded_domain_vertical():
   # Define variable x
    x = np.linspace(0, 2 * np.pi, 500)
    
    # Define functions
    h_x = np.cos(x)
    k_x = np.sin(x)
    
    # Create a figure and two subplots
    fig, axs = plt.subplots(2, 1, figsize=(12, 6)) #2 rows, 1 column
    
    # Top subplot
    axs[0].plot(x, h_x, label=r"$h(x) = \cos(x)$", color='blue')
    axs[0].set_title(r"$h(x) = \cos(x)$")
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("h(x)")
    axs[0].legend()
    
    # Bottom subplot
    axs[1].plot(x, k_x, label=r"$k(x) = \sin(x)$", color='green')
    axs[1].set_title(r"$k(x) = \sin(x)$")
    axs[1].set_xlabel("x")
    axs[1].set_ylabel("k(x)")
    axs[1].legend()
    
    # Set domain from 0 to 4π
    axs[0].set_xlim(0, 4 * np.pi)
    axs[1].set_xlim(0, 4 * np.pi)

    #Adjust layout
    plt.tight_layout()

    plt.show()