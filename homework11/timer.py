import numpy as np
import time


def orbital_period_timer(a):
    start = time.time() # Begin timer
    orbital_period(a)
    end = time.time() # End timer
    return print(end - start)  # Print the time elapsed in between