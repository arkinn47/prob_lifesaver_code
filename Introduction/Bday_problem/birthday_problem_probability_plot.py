"""
This page has code to print a plot showing the probabilities that
at least two people in a group have the same birthday, for a given 
number of people.
"""

import matplotlib.pyplot as plt
import math
import numpy as np

X = np.linspace(0,50,51)
Y = np.array([1 - math.factorial(365)/(math.factorial(365 - int(y))*365**int(y)) for y in X])


plt.xlabel("Number of People")
plt.ylabel("Probability")
plt.title('Probability at Least 2 Birthdays are the Same for # of People')
plt.plot(X,Y, color = 'green', linestyle = 'None',marker='.')
plt.show()