"""This module models the water level graphs to an appropiate degree polynomial.

"""

import matplotlib
import numpy as np

def polyfit(dates, levels, p):

    # convert dates to nummbers
    datenums = matplotlib.dates.date2num(dates)

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(datenums - datenums[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    return poly, datenums[0]

    




